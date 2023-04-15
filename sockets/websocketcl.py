import asyncio
import websockets

async def hello():
    while True:
        uri = "ws://localhost:9990"
        async with websockets.connect(uri) as websocket:
            greeting = await websocket.recv()
            print(f"< {greeting}")

asyncio.get_event_loop().run_until_complete(hello())