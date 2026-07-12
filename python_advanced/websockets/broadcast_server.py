#!/usr/bin/env python3
"""WebSocket server that broadcasts messages to all clients."""

import asyncio
import websockets
from websockets.exceptions import ConnectionClosed


connected_clients = set()


async def handler(websocket):
    """Track one client and broadcast received messages to all clients."""
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            disconnected_clients = set()
            for client in connected_clients:
                try:
                    await client.send(f"B:{message}")
                except ConnectionClosed:
                    disconnected_clients.add(client)
            connected_clients.difference_update(disconnected_clients)
    except ConnectionClosed:
        pass
    finally:
        connected_clients.discard(websocket)


connection_handler = handler


async def main():
    """Start the WebSocket broadcast server."""
    async with websockets.serve(handler, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
