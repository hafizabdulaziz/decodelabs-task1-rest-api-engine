import uuid
import time
import sys
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from contextlib import asynccontextmanager
from loguru import logger
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from app.core.config import settings
from app.core.limiter import limiter
from app.api.v1.products import router as products_router
from app.db.session import engine, Base, async_session
from app.db.models import Product
from sqlalchemy import select

# Setup Loguru
logger.remove()
logger.add(sys.stderr, format="{message}", serialize=True)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        
    # Seed Data
    async with async_session() as session:
        result = await session.execute(select(Product))
        if not result.scalars().first():
            products = [
                Product(title="Laptop", description="High performance laptop", price=1200.0, category="Electronics", stock=5),
                Product(title="Mouse", description="Wireless mouse", price=25.0, category="Electronics", stock=50),
            ]
            session.add_all(products)
            await session.commit()
    yield
    # Shutdown

app = FastAPI(title=settings.PROJECT_NAME, lifespan=lifespan)

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Trusted Host
app.add_middleware(TrustedHostMiddleware, allowed_hosts=["*"])

# Correlation ID and Structured Logging Middleware
@app.middleware("http")
async def add_request_id_and_logging(request: Request, call_next):
    request_id = str(uuid.uuid4())
    start_time = time.time()
    
    # Process request
    response = await call_next(request)
    
    # Calculate latency
    latency = time.time() - start_time
    
    # Log request details
    logger.info({
        "request_id": request_id,
        "method": request.method,
        "path": request.url.path,
        "status_code": response.status_code,
        "latency": f"{latency:.4f}s"
    })
    
    # Add Request ID to response header
    response.headers["X-Request-ID"] = request_id
    
    # Security Headers
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    
    return response

app.include_router(products_router, prefix=settings.API_V1_STR + "/products", tags=["products"])

@app.get("/")
async def root():
    return {"message": f"Welcome to {settings.PROJECT_NAME} API"}
