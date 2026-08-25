import asyncio
import websockets

async def test_ws():
    async with websockets.connect("ws://127.0.0.1:8000/ws") as ws:
        print("Connected!")
        # receive one message
        try:
            msg = await ws.recv()
            print("Received:", msg)
        except Exception as e:
            print("Error recv:", e)

asyncio.run(test_ws())
