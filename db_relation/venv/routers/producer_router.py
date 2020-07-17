from __future__ import annotations

from fastapi import APIRouter

import sqlalchemy as db
import base
from sqlalchemy.orm import sessionmaker
from pydantic import parse_obj_as
from typing import List

from dto.producer import ProducerDTO

from models.products import Product
from models.sellers import Seller
from models.producers import Producer

from repository.producer_repository import ProducerRepository

router = APIRouter()

producer_repository: ProducerRepository = ProducerRepository(base.get_session())

@router.get('/producers', response_model=List[ProducerDTO])
async def get_producer():
    producers = producer_repository.get_all()
    results: List[ProducerDTO]
    results = parse_obj_as(List[ProducerDTO], producers)
    return results


@router.get('/producers/{producer_id}', response_model=ProducerDTO)
async def get_producer(producer_id: int):
    product = producer_repository.get_producer(producer_id)
    return product


@router.post('/producers', response_model=ProducerDTO)
async def create_producer(producer_new: ProducerDTO):
    result: Producer
    result = producer_repository.save_producer(producer_new)
    return result


@router.put('/producers', response_model=ProducerDTO)
async def update_producer(producer_update: ProducerDTO):
    result: Producer
    result = producer_repository.update_producer(producer_update)
    return result


@router.delete('/producers/{producer_id}')
async def create_producer(producer_id: int):
    return {"message": producer_repository.remove_producer(producer_id)}