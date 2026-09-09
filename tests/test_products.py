import pytest

@pytest.mark.asyncio
async def test_create_product(client):
    response = await client.post("/api/v1/products/", json={"title": "Test Product", "description": "Test Desc", "price": 10.5})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Product"
    assert "id" in data

@pytest.mark.asyncio
async def test_get_products(client):
    response = await client.get("/api/v1/products/")
    assert response.status_code == 200
    data = response.json()
    assert "items" in data
    assert "total" in data
    assert isinstance(data["items"], list)

@pytest.mark.asyncio
async def test_get_product(client):
    # Create product first
    post_response = await client.post("/api/v1/products/", json={"title": "Prod_Unique", "price": 5.0})
    product_id = post_response.json()["id"]
    response = await client.get(f"/api/v1/products/{product_id}")
    assert response.status_code == 200
    assert response.json()["title"] == "Prod_Unique"

