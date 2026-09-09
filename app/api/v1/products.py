from fastapi import APIRouter, HTTPException, Depends
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.product import Product, ProductCreate
from app.db.store import store
from app.db.session import async_session

router = APIRouter()

async def get_db():
    async with async_session() as session:
        yield session

@router.post("/", response_model=Product)
async def create_product(product_in: ProductCreate, db: AsyncSession = Depends(get_db)):
    return await store.create(db, product_in)

@router.get("/", response_model=List[Product])
async def get_products(db: AsyncSession = Depends(get_db)):
    return await store.get_all(db)

@router.get("/{product_id}", response_model=Product)
async def get_product(product_id: int, db: AsyncSession = Depends(get_db)):
    product = await store.get_by_id(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
