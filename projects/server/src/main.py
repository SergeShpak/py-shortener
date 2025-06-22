"""Server entry point."""

import asyncio

import uvicorn
from fastapi import FastAPI

from .routers import shortener

app = FastAPI()

app.include_router(shortener.router)

def main() -> None:
    """Server entry point function."""
    asyncio.run(start_server())

async def start_server() -> None:
    """Start the FastAPI server asynchronously."""
    config = uvicorn.Config(
        "src.main:app",
        host="localhost",
        port=8080,
        reload=True,
        log_level="info",
    )
    server = uvicorn.Server(config)
    await server.serve()

if __name__ == "__main__":
    main()
