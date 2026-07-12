#!/usr/bin/env python3
"""ASGI WebSocket echo application."""

from pathlib import Path

from starlette.applications import Starlette
from starlette.responses import FileResponse
from starlette.routing import Route, WebSocketRoute
from starlette.websockets import WebSocketDisconnect


BASE_DIR = Path(__file__).resolve().parent


async def homepage(request):
    """Return the browser WebSocket client."""
    return FileResponse(BASE_DIR / "index.html")


async def styles(request):
    """Return the stylesheet."""
    return FileResponse(BASE_DIR / "styles.css")


async def javascript(request):
    """Return the browser client script."""
    return FileResponse(BASE_DIR / "chat.js")


async def websocket_endpoint(websocket):
    """Accept WebSocket messages and echo them back to the sender."""
    await websocket.accept()
    try:
        while True:
            message = await websocket.receive_text()
            await websocket.send_text(message)
    except WebSocketDisconnect:
        pass


app = Starlette(routes=[
    Route("/", homepage),
    Route("/styles.css", styles),
    Route("/chat.js", javascript),
    WebSocketRoute("/ws", websocket_endpoint),
])
