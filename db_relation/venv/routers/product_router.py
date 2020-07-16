from __future__ import annotations

from fastapi import APIRouter

import sqlalchemy as db
# from base import Base
import base
from sqlalchemy.orm import sessionmaker
from pydantic import parse_obj_as
from typing import List

from dto.product import ProductUpdateDTO, ProductDto, ProductCreateDto, SellerCreateProductDto

from models.products import Product
from models.sellers import Seller
from models.producers import Producer

from repository.product_repository import ProductRepository

router = APIRouter()

product_repository: ProductRepository = ProductRepository(base.get_session())

@router.get('/products', response_model=List[ProductDto])
async def get_products():
    products = product_repository.get_all()
    results: List[ProductDto]
    results = parse_obj_as(List[ProductDto], products)
    return results


@router.get('/products/{product_id}', response_model=ProductDto)
async def get_product(product_id: int):
    product = product_repository.get_product(product_id)
    return product


@router.post('/products')
async def create_product(seller_create_product: SellerCreateProductDto):
    result: Product
    result = product_repository.save_product(seller_create_product.seller_id, seller_create_product.productCreate)
    return result


@router.put('/products')
async def create_product(product_update: ProductUpdateDTO):
    result: Product
    result = product_repository.save_product(product_update)
    return result


@router.delete('/products/{product_id}')
async def create_product(product_id: int):
    return {"message": product_repository.remove_product(product_id)}