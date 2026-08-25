#!/usr/bin/env python3
"""
FastAPI Backend for Gemini Live Web Voice Assistant.
Bridges Browser WebSocket (with Native WebRTC Echo Cancellation) to Gemini Live API.
"""

import os
import sys
import json
import base64
import asyncio
import wave
from datetime import datetime
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

from google import genai
from google.genai import types

app = FastAPI()

script_dir = os.path.dirname(os.path.abspath(__file__))
repo_root = os.path.abspath(os.path.join(script_dir, "../../../.."))

def get_repo_context():
    agents_path = os.path.join(repo_root, "AGENTS.md")
    state_path = os.path.join(repo_root, "learner", "LEARNING_STATE.md")
    
    agents_content = ""
    if os.path.exists(agents_path):
        with open(agents_path, "r", encoding="utf-8") as f:
            agents_content = f.read()
            
    state_content = ""
    if os.path.exists(state_path):
        with open(state_path, "r", encoding="utf-8") as f:
            state_content = f.read()
            
    return agents_content, state_content

@app.get("/", response_class=HTMLResponse)
async def get_index():
    html_path = os.path.join(script_dir, "web", "index.html")
    with open(html_path, "r", encoding="utf-8") as f:
        return f.read()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        await websocket.send_json({"type": "text", "content": "❌ Error: GEMINI_API_KEY not set in .env file."})
        await websocket.close()
        return

    agents_content, state_content = get_repo_context()
    sys_instruction = f"""You are an expert English speaking coach conducting a live real-time voice session.
Authoritative learner rules:
---
{agents_content}
---
Current Learner State:
---
{state_content}
---
CRITICAL RULES:
1. Speak in concise spoken turns (1-2 sentences at a time). Never give a long monologue.
2. Let the learner speak and finish their thoughts.
3. Act as an authentic speaking partner.
"""

    client = genai.Client(api_key=api_key)

    candidate_models = [
        "gemini-3.1-flash-live-preview",
    ]

    if hasattr(types.Part, "from_text"):
        sys_part = types.Part.from_text(text=sys_instruction)
    else:
        sys_part = types.Part(text=sys_instruction)

    config = types.LiveConnectConfig(
        response_modalities=["AUDIO"],
        speech_config=types.SpeechConfig(
            voice_config=types.VoiceConfig(
                prebuilt_voice_config=types.PrebuiltVoiceConfig(
                    voice_name="Puck"
                )
            )
        ),
        system_instruction=types.Content(parts=[sys_part])
    )

    transcript_log = []
    user_audio_bytes = bytearray()
    ai_audio_bytes = bytearray()
    session_start_time = datetime.now()

    for model_id in candidate_models:
        try:
            print(f"[Web Live] Connecting to {model_id}...", flush=True)
            async with client.aio.live.connect(model=model_id, config=config) as session:
                print(f"[Web Live] Connected successfully with {model_id}!", flush=True)

                # Send an initial message to kick off the conversation
                try:
                    if hasattr(session, "send_client_content"):
                        await session.send_client_content(turns=[{"role": "user", "parts": [{"text": "Hello, I am ready. Please introduce yourself briefly and let's start the session."}]}], turn_complete=True)
                    elif hasattr(session, "send"):
                        await session.send(input="Hello, I am ready. Please introduce yourself briefly and let's start the session.", end_of_turn=True)
                except Exception as e:
                    print(f"[Web Live] Initial message error: {e}", flush=True)

                async def receive_from_browser():
                    try:
                        while True:
                            data = await websocket.receive()
                            if "bytes" in data and data["bytes"]:
                                audio_bytes = data["bytes"]
                                user_audio_bytes.extend(audio_bytes)
                                blob = types.Blob(data=audio_bytes, mime_type="audio/pcm;rate=16000")
                                if hasattr(session, "send_realtime_input"):
                                    await session.send_realtime_input(audio=blob)
                                elif hasattr(session, "send"):
                                    await session.send(input={"data": audio_bytes, "mime_type": "audio/pcm;rate=16000"})
                            elif "text" in data and data["text"]:
                                try:
                                    msg = json.loads(data["text"])
                                    if msg.get("type") == "client_turn_complete":
                                        if hasattr(session, "send_client_content"):
                                            await session.send_client_content(turn_complete=True)
                                        elif hasattr(session, "send"):
                                            await session.send(end_of_turn=True)
                                except Exception as e:
                                    print(f"[JSON Parse Error]: {e}", flush=True)
                    except WebSocketDisconnect:
                        pass
                    except Exception as e:
                        print(f"[Browser Receive Error]: {e}", flush=True)

                async def send_to_browser():
                    try:
                        while True:
                            async for response in session.receive():
                                if response.server_content is not None:
                                    content = response.server_content
                                    if getattr(content, "interrupted", False):
                                        await websocket.send_json({"type": "interrupted"})
                                    
                                    if getattr(content, "turn_complete", False):
                                        await websocket.send_json({"type": "turn_complete"})
                                        continue
                                        
                                    if getattr(content, "interim_input_transcription", None) is not None:
                                        # Not doing interim to avoid spamming the UI
                                        pass
                                        
                                    if getattr(content, "input_transcription", None) is not None:
                                        text = content.input_transcription.text
                                        if text:
                                            transcript_log.append(f"User: {text}")
                                            await websocket.send_json({"type": "user_text", "content": text})

                                    if getattr(content, "model_turn", None) is not None:
                                        for part in content.model_turn.parts:
                                            if part.text:
                                                transcript_log.append(f"AI: {part.text}")
                                                await websocket.send_json({"type": "text", "content": part.text})
                                            if part.inline_data and part.inline_data.data:
                                                ai_audio_bytes.extend(part.inline_data.data)
                                                b64 = base64.b64encode(part.inline_data.data).decode("utf-8")
                                                await websocket.send_json({"type": "audio", "data": b64})

                                elif getattr(response, "data", None) is not None:
                                    ai_audio_bytes.extend(response.data)
                                    b64 = base64.b64encode(response.data).decode("utf-8")
                                    await websocket.send_json({"type": "audio", "data": b64})
                    except WebSocketDisconnect:
                        pass
                    except Exception as e:
                        print(f"[Gemini Stream Error]: {e}", flush=True)

                browser_recv_task = asyncio.create_task(receive_from_browser(), name="recv")
                browser_send_task = asyncio.create_task(send_to_browser(), name="send")

                done, pending = await asyncio.wait(
                    [browser_recv_task, browser_send_task],
                    return_when=asyncio.FIRST_COMPLETED
                )
                for task in done:
                    print(f"[Debug] Task finished: {task.get_name()}, Exception: {task.exception()}", flush=True)
                for task in pending:
                    task.cancel()
                break

        except Exception as e:
            print(f"[Model {model_id} error]: {e}")
            continue

    save_session(repo_root, session_start_time, transcript_log, user_audio_bytes, ai_audio_bytes)

def save_session(repo_root: str, start_time: datetime, transcript_log: list, user_audio_bytes: bytearray, ai_audio_bytes: bytearray):
    if not transcript_log:
        return
    date_str = start_time.strftime("%Y-%m-%d")
    timestamp_slug = start_time.strftime("%Y-%m-%d-%H%M")
    filename = f"{timestamp_slug}-speaking-live-web.md"
    file_path = os.path.join(repo_root, "sessions", filename)
    
    transcript_text = "\n".join(transcript_log)
    content = f"""# Session — Live Speaking (Web Client)

Date: {date_str}
Mode: Real-time Gemini Live Voice (Clean Audio Pipeline)

## Skill evidence (Live Speaking)
- Real-time conversational responsiveness

## Transcript & Summary
```text
{transcript_text}
```
"""
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"\n✅ Session log saved to: sessions/{filename}")

    if user_audio_bytes:
        user_wav_path = os.path.join(repo_root, "sessions", f"{timestamp_slug}-speaking-live-web-user.wav")
        with wave.open(user_wav_path, "wb") as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(16000)
            wf.writeframes(user_audio_bytes)
        print(f"✅ User audio saved to: sessions/{timestamp_slug}-speaking-live-web-user.wav")

    if ai_audio_bytes:
        ai_wav_path = os.path.join(repo_root, "sessions", f"{timestamp_slug}-speaking-live-web-ai.wav")
        with wave.open(ai_wav_path, "wb") as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(24000)
            wf.writeframes(ai_audio_bytes)
        print(f"✅ AI audio saved to: sessions/{timestamp_slug}-speaking-live-web-ai.wav")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
