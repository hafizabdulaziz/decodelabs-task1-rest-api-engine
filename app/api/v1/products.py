import re
from fastapi import APIRouter, HTTPException, Depends, Query, Request, Path
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.product import Product, ProductCreate, ProductPaginated
from app.db.store import store
from app.db.session import async_session
from app.core.limiter import limiter

router = APIRouter()

def sanitize_numeric(value: Optional[str]) -> Optional[float]:
    if value is None:
        return None
    # Remove non-numeric characters except decimal point
    cleaned = re.sub(r'[^0-9.]', '', str(value))
    try:
        return float(cleaned)
    except ValueError:
        return None

async def get_db():
    async with async_session() as session:
        yield session

@router.post("/", response_model=Product)
@limiter.limit("5/minute")
async def create_product(request: Request, product_in: ProductCreate, db: AsyncSession = Depends(get_db)):
    return await store.create(db, product_in)

@router.get("/", response_model=ProductPaginated)
async def get_products(
    db: AsyncSession = Depends(get_db),
    category: Optional[str] = None,
    search: Optional[str] = None,
    min_price: Optional[str] = Query(None, description="Minimum price (e.g., 100 or '100$')"),
    max_price: Optional[str] = Query(None, description="Maximum price (e.g., 500 or '500$')"),
    sort_by: Optional[str] = Query(None, enum=["price_asc", "price_desc", "created_at"]),
    page: int = Query(1, ge=1, description="Page number"),
    size: int = Query(10, ge=1, le=100, description="Page size")
):
    min_price_float = sanitize_numeric(min_price)
    max_price_float = sanitize_numeric(max_price)
    
    items, total = await store.get_all(db, category, search, min_price_float, max_price_float, sort_by, page, size)
    return {"total": total, "page": page, "size": size, "items": items}

@router.get("/{product_id}", response_model=Product, responses={404: {"description": "Product not found"}})
async def get_product(product_id: int = Path(..., description="ID of the product"), db: AsyncSession = Depends(get_db)):
    product = await store.get_by_id(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
