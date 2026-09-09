import pytest

@pytest.mark.asyncio
async def test_create_product(client):
    response = await client.post("/api/v1/products/", json={"name": "Test Product", "description": "Test Desc", "price": 10.5})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Product"
    assert "id" in data

@pytest.mark.asyncio
async def test_get_products(client):
    response = await client.get("/api/v1/products/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_get_product(client):
    # Create product first
    await client.post("/api/v1/products/", json={"name": "Prod_Unique", "price": 5.0})
    response = await client.get("/api/v1/products/2")
    assert response.status_code == 200
    assert response.json()["name"] == "Prod_Unique"
