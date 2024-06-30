import aioconsole
import asyncio
import websockets

async def receive_messages(websocket):
    while True:
        message = await websocket.recv()
        print(f"\nReceived: {message}")

async def send_messages(websocket):
    while True:
        message = await aioconsole.ainput("Enter message: ")
        await websocket.send(message)

async def main():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        await asyncio.gather(
            receive_messages(websocket),
            send_messages(websocket)
        )

asyncio.get_event_loop().run_until_complete(main())
