#!/usr/bin/env python3
"""WebSocket server with basic message validation."""

import asyncio
import websockets
from websockets.exceptions import ConnectionClosed


async def handler(websocket):
    """Validate incoming messages and send a response for each one."""
    try:
        async for message in websocket:
            if len(message.strip()) == 0:
                await websocket.send("ERR:EMPTY")
            else:
                await websocket.send(f"OK:{message}")
    except ConnectionClosed:
        pass


connection_handler = handler


async def main():
    """Start the WebSocket validation server."""
    async with websockets.serve(handler, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
