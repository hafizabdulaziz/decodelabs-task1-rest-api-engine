from fastapi import FastAPI
from app.core.config import settings
from app.api.v1.products import router as products_router

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(products_router, prefix=settings.API_V1_STR + "/products", tags=["products"])

@app.get("/")
async def root():
    return {"message": f"Welcome to {settings.PROJECT_NAME} API"}
