import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app

@pytest.fixture
async def client():
    # Use ASGITransport to connect httpx directly to the FastAPI app
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        yield client
