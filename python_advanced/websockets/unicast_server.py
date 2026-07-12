#!/usr/bin/env python3
"""WebSocket server that replies only to the sender."""

import asyncio
import websockets
from websockets.exceptions import ConnectionClosed


connected_clients = set()


async def handler(websocket):
    """Track one client and send unicast responses to its messages."""
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            await websocket.send(f"U:{message}")
    except ConnectionClosed:
        pass
    finally:
        connected_clients.remove(websocket)


connection_handler = handler


async def main():
    """Start the WebSocket unicast server."""
    async with websockets.serve(handler, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
