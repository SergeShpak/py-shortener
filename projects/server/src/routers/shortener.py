"""URL Shortener API Router.

This module contains FastAPI routes for URL shortening functionality.
It provides endpoints for creating, retrieving, and managing shortened URLs.

Example:
    The router can be included in the main FastAPI app:
    ```python
    from fastapi import FastAPI
    from .routers.shortener import router as shortener_router

    app = FastAPI()
    app.include_router(shortener_router, prefix="/s", tags=["shortener"])
    ```
"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/{url_id}")
async def get_full_url(url_id: str) -> dict[str, str]:
    """Retrieves a full URL using its slug."""
    return {"id": url_id}
