#!/usr/bin/python3
"""Minimal WebSocket echo server."""

import asyncio
import websockets


async def connection_handler(websocket):
    """Echo every text message received on the WebSocket connection."""
    async for message in websocket:
        await websocket.send(message)


async def main():
    """Start the WebSocket echo server."""
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
