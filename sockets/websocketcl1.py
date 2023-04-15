import asyncio
import websockets

async def hello():
    while True:
        uri = "ws://localhost:9990"
        async with websockets.connect(uri) as websocket:
            name = input("What's your name? ")

            await websocket.send(name)
            print(f"> {name}")

asyncio.get_event_loop().run_until_complete(hello())