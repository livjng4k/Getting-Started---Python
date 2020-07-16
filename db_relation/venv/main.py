from __future__ import annotations
import sqlalchemy as db
from fastapi import Depends, FastAPI, Header, HTTPException

from routers import product_router

app = FastAPI()

app.include_router(product_router.router, tags=["Products"])