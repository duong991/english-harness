#!/usr/bin/env python3
"""
Gemini Live Voice-to-Voice Practice Assistant for English Learning Harness.
Connects real-time microphone and speaker streams to Gemini Multimodal Live API.
Includes Software Echo Suppression to completely eliminate acoustic feedback loops when using speakers.
Automatically grounds the conversation in AGENTS.md and LEARNING_STATE.md,
and writes structured session logs to sessions/ upon completion.
"""

import os
import sys
import time
import asyncio
import argparse
import traceback
from datetime import datetime

# Load environment variables from .env if present
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

def check_dependencies():
    missing = []
    try:
        import pyaudio
    except ImportError:
        missing.append("pyaudio")
    try:
        import google.genai
    except ImportError:
        missing.append("google-genai")
    
    if missing:
        print("❌ Missing required dependencies: " + ", ".join(missing))
        print("💡 Run the following to install:")
        print(f"   pip install -r {os.path.join(os.path.dirname(__file__), 'requirements.txt')}")
        print("   (On macOS, if pyaudio fails: 'brew install portaudio && pip install pyaudio')")
        return False
    return True

def get_repo_context():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.abspath(os.path.join(script_dir, "../../../.."))
    
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
            
    # Load the latest session transcript to maintain context
    sessions_dir = os.path.join(repo_root, "sessions")
    past_transcript = ""
    if os.path.exists(sessions_dir):
        session_files = [f for f in os.listdir(sessions_dir) if f.endswith(".md")]
        if session_files:
            latest_session = sorted(session_files)[-1]
            try:
                with open(os.path.join(sessions_dir, latest_session), "r", encoding="utf-8") as f:
                    past_transcript = f.read()
            except Exception:
                pass

    return repo_root, agents_content, state_content, past_transcript

def build_system_instruction(topic: str, agents_content: str, state_content: str, past_transcript: str) -> str:
    transcript_section = ""
    if past_transcript:
        transcript_section = f"\nPrevious Session Context (for continuity):\n---\n{past_transcript}\n---\n"

    return f"""You are an expert English speaking coach conducting a live real-time voice session.
You are running within the English Learning Harness.

Authoritative learner rules and context:
---
{agents_content}
---
Current Learner State:
---
{state_content}
---{transcript_section}

TODAY'S LIVE SPEAKING SESSION:
- Topic/Scenario: {topic}
- Mode: Spontaneous 2-way conversation practice.
- Voice Tone: Natural, encouraging, concise, professional English.

CRITICAL RULES FOR YOU DURING LIVE VOICE CALL:
1. Speak in concise spoken turns (1-2 sentences at a time). Never give a long monologue.
2. Let the learner speak first and finish their thoughts. Do not interrupt or finish their sentences.
3. Act as a realistic conversation partner in the chosen scenario. Ask relevant follow-up questions or request clarification.
4. During the live conversation, keep the conversation moving naturally. Do NOT pause every turn to lecture on grammar or vocabulary.
5. At the very end of the conversation (when the learner says goodbye or time is up), provide a short 30-second spoken summary with:
   - 1 compliment on communication/task completion
   - 1-2 high-impact collocation/word upgrades
   - 1 pronunciation/IPA tip.
6. If the learner struggles to express an idea or asks for explanation, you may use Vietnamese to clarify or assist.
7. DO NOT start with an introductory greeting. Jump directly into the conversation as a continuation of previous context or immediately prompt the learner's response.
"""

async def run_live_session(topic: str, duration_mins: int, custom_model: str = ""):
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("❌ Error: GEMINI_API_KEY environment variable is not set.")
        print("💡 Set it using: export GEMINI_API_KEY='your_api_key_here' or add it to a .env file.")
        sys.exit(1)

    import pyaudio
    from google import genai
    from google.genai import types

    repo_root, agents_content, state_content, past_transcript = get_repo_context()
    sys_instruction = build_system_instruction(topic, agents_content, state_content, past_transcript)

    # Audio configuration
    AUDIO_FORMAT = pyaudio.paInt16
    AUDIO_CHANNELS = 1
    INPUT_SAMPLE_RATE = 16000
    OUTPUT_SAMPLE_RATE = 24000
    CHUNK_SIZE = 1024

    p = pyaudio.PyAudio()
    
    # Input stream (Microphone)
    input_stream = p.open(
        format=AUDIO_FORMAT,
        channels=AUDIO_CHANNELS,
        rate=INPUT_SAMPLE_RATE,
        input=True,
        frames_per_buffer=CHUNK_SIZE
    )
    
    # Output stream (Speaker)
    output_stream = p.open(
        format=AUDIO_FORMAT,
        channels=AUDIO_CHANNELS,
        rate=OUTPUT_SAMPLE_RATE,
        output=True,
        frames_per_buffer=CHUNK_SIZE
    )

    client = genai.Client(api_key=api_key)

    # Build system instruction content safely across SDK versions
    if hasattr(types.Part, "from_text"):
        sys_part = types.Part.from_text(text=sys_instruction)
    else:
        sys_part = types.Part(text=sys_instruction)

    config = types.LiveConnectConfig(
        response_modalities=["AUDIO"],
        speech_config=types.SpeechConfig(
            voice_config=types.VoiceConfig(
                prebuilt_voice_config=types.PrebuiltVoiceConfig(
                    voice_name="Puck"  # Clear, natural voice
                )
            )
        ),
        system_instruction=types.Content(parts=[sys_part])
    )

    print("\n" + "="*60)
    print(f"🎙️  GEMINI LIVE VOICE SESSION: '{topic}'")
    print(f"⏱️  Duration: ~{duration_mins} minutes (Press Ctrl+C anytime to finish)")
    print("🛡️  Acoustic Echo Suppression: ENABLED (No speaker feedback loop)")
    print("="*60)
    print("⏳ Connecting to Gemini Live API...")

    if custom_model:
        candidate_models = [custom_model]
    else:
        candidate_models = [
            "gemini-3.1-flash-live-preview",
        ]

    transcript_log = []
    session_start_time = datetime.now()
    session_connected = False

    for model_id in candidate_models:
        try:
            print(f"🔄 Attempting connection with model: {model_id}...")
            async with client.aio.live.connect(model=model_id, config=config) as session:
                session_connected = True
                print(f"\n🟢 CONNECTED with {model_id}! Start speaking into your microphone now...\n")

                audio_queue = asyncio.Queue()
                stop_event = asyncio.Event()
                loop = asyncio.get_running_loop()
                
                # Shared state for Echo Suppression
                is_ai_speaking = False
                last_ai_play_time = 0.0

                async def send_audio_loop():
                    """Captures mic audio and streams it to Gemini. Suppresses input while AI is speaking."""
                    nonlocal is_ai_speaking, last_ai_play_time
                    while not stop_event.is_set():
                        try:
                            # Read microphone audio
                            data = await loop.run_in_executor(None, input_stream.read, CHUNK_SIZE, False)
                            
                            # Echo Guard: If AI is actively speaking or just finished (<0.3s ago), drop mic input
                            if is_ai_speaking or (time.time() - last_ai_play_time < 0.35):
                                await asyncio.sleep(0.005)
                                continue

                            if data and len(data) > 0:
                                blob = types.Blob(data=data, mime_type=f"audio/pcm;rate={INPUT_SAMPLE_RATE}")
                                if hasattr(session, "send_realtime_input"):
                                    await session.send_realtime_input(audio=blob)
                                else:
                                    await session.send(input={"data": data, "mime_type": f"audio/pcm;rate={INPUT_SAMPLE_RATE}"})
                            await asyncio.sleep(0.001)
                        except Exception:
                            if not stop_event.is_set():
                                await asyncio.sleep(0.01)

                async def play_audio_loop():
                    """Plays audio chunks in a separate thread to never freeze the event loop."""
                    nonlocal is_ai_speaking, last_ai_play_time
                    while not stop_event.is_set():
                        try:
                            audio_chunk = await audio_queue.get()
                            if audio_chunk:
                                is_ai_speaking = True
                                last_ai_play_time = time.time()
                                await asyncio.to_thread(output_stream.write, audio_chunk)
                                last_ai_play_time = time.time()
                            audio_queue.task_done()
                            
                            # If queue is now empty, release the mic lock after a short room reverb cooldown
                            if audio_queue.empty():
                                await asyncio.sleep(0.35)
                                if audio_queue.empty() and (time.time() - last_ai_play_time >= 0.35):
                                    is_ai_speaking = False

                        except asyncio.CancelledError:
                            break
                        except Exception:
                            if not stop_event.is_set():
                                await asyncio.sleep(0.01)

                async def receive_audio_loop():
                    """Continuously receives response chunks from Gemini across all turns."""
                    nonlocal is_ai_speaking
                    while not stop_event.is_set():
                        try:
                            async for response in session.receive():
                                if response.server_content is not None:
                                    content = response.server_content
                                    
                                    # Handle user barge-in (interruption)
                                    if getattr(content, "interrupted", False):
                                        while not audio_queue.empty():
                                            try:
                                                audio_queue.get_nowait()
                                                audio_queue.task_done()
                                            except Exception:
                                                break
                                        is_ai_speaking = False

                                    # Turn complete signal - keep listening for future turns!
                                    if getattr(content, "turn_complete", False):
                                        continue

                                    if content.model_turn is not None:
                                        for part in content.model_turn.parts:
                                            if part.text:
                                                print(part.text, end="", flush=True)
                                                transcript_log.append(f"AI: {part.text}")
                                            if part.inline_data and part.inline_data.data:
                                                await audio_queue.put(part.inline_data.data)

                                if getattr(response, "data", None) is not None:
                                    await audio_queue.put(response.data)

                        except asyncio.CancelledError:
                            break
                        except Exception:
                            if not stop_event.is_set():
                                await asyncio.sleep(0.05)

                send_task = asyncio.create_task(send_audio_loop())
                receive_task = asyncio.create_task(receive_audio_loop())
                play_task = asyncio.create_task(play_audio_loop())

                # Wait for target duration or until cancelled
                try:
                    if duration_mins > 0:
                        await asyncio.sleep(duration_mins * 60)
                        print("\n\n⏰ Session time limit reached. Wrapping up...")
                    else:
                        while not stop_event.is_set():
                            await asyncio.sleep(0.5)
                finally:
                    stop_event.set()
                    send_task.cancel()
                    receive_task.cancel()
                    play_task.cancel()
                    await asyncio.gather(send_task, receive_task, play_task, return_exceptions=True)
            
            # If we reached here without exception, session finished naturally
            break

        except (KeyboardInterrupt, asyncio.CancelledError):
            print("\n\n🛑 Ending Live session...")
            break
        except Exception as e:
            print(f"⚠️ Model {model_id} connection issue ({e}). Trying next candidate...")
            continue
        finally:
            if session_connected:
                # Cleanup audio
                try:
                    input_stream.stop_stream()
                    input_stream.close()
                    output_stream.stop_stream()
                    output_stream.close()
                    p.terminate()
                except Exception:
                    pass

    # Post-session saving only if session connected and ran
    if session_connected:
        save_session_log(repo_root, topic, session_start_time, transcript_log)
    else:
        print("❌ Could not establish Live connection with available models. Please verify your GEMINI_API_KEY has Gemini 2.0 Live API access.")

def save_session_log(repo_root: str, topic: str, start_time: datetime, transcript_log: list):
    date_str = start_time.strftime("%Y-%m-%d")
    timestamp_slug = start_time.strftime("%Y-%m-%d-%H%M")
    topic_slug = topic.replace(" ", "-").lower()[:30]
    
    sessions_dir = os.path.join(repo_root, "sessions")
    os.makedirs(sessions_dir, exist_ok=True)
    
    filename = f"{timestamp_slug}-speaking-live-{topic_slug}.md"
    file_path = os.path.join(sessions_dir, filename)
    
    transcript_text = "\n".join(transcript_log) if transcript_log else "Real-time audio stream exchanged."
    
    content = f"""# Session — Live Speaking: {topic}

Date: {date_str}
Mode: Real-time Gemini Live Voice Session
Duration: ~{int((datetime.now() - start_time).total_seconds() / 60)} minutes

## Goal link and task
- Topic: {topic}
- Mode: Unscripted real-time two-way voice dialogue

## Skill evidence (Live Speaking)
- Real-time conversational responsiveness
- Live auditory comprehension and spontaneous retrieval

## Transcript & Summary
```text
{transcript_text}
```

## Follow-up & Next Action
- Review recurring pauses or pronunciation issues identified in call.
- Schedule parallel topic check in `reviews/QUEUE.md`.
"""

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    print("\n" + "="*60)
    print(f"✅ Session log saved to: sessions/{filename}")
    print("🎯 Updated repository with live speaking evidence!")
    print("="*60 + "\n")

def main():
    parser = argparse.ArgumentParser(description="Start a Gemini Live Voice Speaking Session")
    parser.add_argument("-t", "--topic", type=str, default="Project and Daily Work Discussion", help="Speaking scenario/topic")
    parser.add_argument("-d", "--duration", type=int, default=5, help="Target duration in minutes (default: 5)")
    parser.add_argument("-m", "--model", type=str, default="", help="Custom model ID (e.g. gemini-3.1-flash-live-preview)")
    args = parser.parse_args()

    if not check_dependencies():
        sys.exit(1)

    try:
        asyncio.run(run_live_session(args.topic, args.duration, args.model))
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")

if __name__ == "__main__":
    main()
