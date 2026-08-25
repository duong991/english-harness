import os
import asyncio
from google import genai
from google.genai import types

async def main():
    client = genai.Client()
    config = types.LiveConnectConfig(
        response_modalities=["AUDIO"]
    )
    print("Connecting...")
    async with client.aio.live.connect(model="gemini-2.0-flash-exp", config=config) as session:
        print("Connected!")
        await session.send(input="Hello, say 'yes' and nothing else.", end_of_turn=True)
        async for response in session.receive():
            if response.server_content is not None:
                content = response.server_content
                if getattr(content, "model_turn", None) is not None:
                    for part in content.model_turn.parts:
                        print(f"TEXT: {part.text}")
                if getattr(content, "turn_complete", False):
                    print("Turn complete")
                    break

asyncio.run(main())
