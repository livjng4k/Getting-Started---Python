from __future__ import annotations

from fastapi import APIRouter

import sqlalchemy as db
import base
from sqlalchemy.orm import sessionmaker
from pydantic import parse_obj_as
from typing import List

from dto.seller import SellerCreateDto, SellerDetailDto
from dto.product import ProductDto

from models.products import Product
from models.sellers import Seller

from repository.seller_repository import SellerRepository

router = APIRouter()

seller_repository: SellerRepository = SellerRepository(base.get_session())

@router.get('/sellers', response_model=List[SellerDetailDto])
async def get_seller():
    sellers = seller_repository.get_all()
    results: List[SellerDetailDto]
    results = parse_obj_as(List[SellerDetailDto], sellers)
    return results


@router.get('/sellers/{seller_id}', response_model=SellerDetailDto)
async def get_seller(seller_id: int):
    product = seller_repository.get_seller(seller_id)
    return product


@router.post('/sellers', response_model=SellerDetailDto)
async def create_seller(seller_new: SellerCreateDto):
    result: Seller
    result = seller_repository.save_seller(seller_new)
    return result


@router.put('/sellers', response_model=SellerDetailDto)
async def update_seller(seller_update: SellerDetailDto):
    result: Seller
    result = seller_repository.update_seller(seller_update)
    return result


@router.delete('/sellers/{seller_id}')
async def create_seller(seller_id: int):
    return {"message": seller_repository.remove_seller(seller_id)}


@router.get('/sellers/{seller_id}/products', response_model=List[ProductDto])
async def get_seller_products(seller_id: int):
    products = seller_repository.get_all_product(seller_id)
    results: List[ProductDto]
    results = parse_obj_as(List[ProductDto], products)
    return results
