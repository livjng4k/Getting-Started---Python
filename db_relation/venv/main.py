from __future__ import annotations
import sqlalchemy as db
from fastapi import Depends, FastAPI, Header, HTTPException

from routers import product_router, producer_router, seller_router

app = FastAPI()

app.include_router(product_router.router, tags=["Products"])
app.include_router(producer_router.router, tags=["Producers"])
app.include_router(seller_router.router, tags=["Sellers"])