import asyncio
import websockets

# Set to store all connected clients
connected = set()

async def chat(websocket, path):
    # Register the client
    connected.add(websocket)
    try:
        async for message in websocket:
            # Broadcast the message to all connected clients
            for conn in connected:
                if conn != websocket:
                    await conn.send(f"User{id(websocket) % 1000}: {message}")
    finally:
        # Unregister the client
        connected.remove(websocket)

# Start the server
start_server = websockets.serve(chat, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
