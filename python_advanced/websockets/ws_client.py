#!/usr/bin/env python3
"""Minimal WebSocket client."""

import asyncio
import os
import websockets


async def connect_and_send(uri: str, text: str) -> str:
    """Send one text message to a WebSocket server and return its response."""
    async with websockets.connect(uri) as websocket:
        await websocket.send(text)
        return await websocket.recv()


async def main():
    """Connect to the local echo server and print the response."""
    uri = os.environ.get("WS_URI", "ws://localhost:8765")
    response = await connect_and_send(uri, "demo")
    print(response, end="")


if __name__ == "__main__":
    asyncio.run(main())
