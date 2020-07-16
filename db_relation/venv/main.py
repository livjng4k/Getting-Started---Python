from __future__ import annotations
import sqlalchemy as db
import shutil
import os
from base import Base
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI, File, UploadFile
from pydantic import parse_obj_as
from typing import List

from dto.product import ProductUpdateDTO, ProductDto, ProductCreateDto, SellerCreateProductDto

from models.products import Product
from models.sellers import Seller
from models.producers import Producer

from repository.product_repository import ProductRepository

# from fastapi.staticfiles import StaticFiles
# from starlette.responses import RedirectResponse


app = FastAPI()
# app.mount("/static", StaticFiles(directory="static"), name="static")

session: db.orm.session = None
product_repository: ProductRepository = None

@app.on_event("startup")
async def startup_event():
    global session
    engine = db.create_engine('sqlite:///example_db.db', echo = False)
    Base.metadata.create_all(engine)
    Session: db.orm.session.sessionmaker = sessionmaker(bind=engine)
    sess: db.orm.Session = Session()
    session = sess
    session.execute("PRAGMA foreign_keys = 1")

    global product_repository
    product_repository = ProductRepository(sess)


@app.get('/product', response_model=List[ProductDto])
async def get_products():
    products = product_repository.get_all()
    results: List[ProductDto]
    results = parse_obj_as(List[ProductDto], products)
    return results


@app.get('/product/{product_id}', response_model=ProductDto)
async def get_product(product_id: int):
    product = product_repository.get_product(product_id)
    return product


@app.post('/product')
async def create_produt(seller_create_product: SellerCreateProductDto):
    result: Product
    result = product_repository.save_product(product_new)
    return result


@app.put('/product')
async def create_produt(product_update: ProductUpdateDTO):
    result: Product
    result = product_repository.save_product(product_update)
    return result


@app.delete('/product/{product_id}')
async def create_produt(product_id: int):
    return {"message": product_repository.remove_product(product_id)}



#
# @app.post('/up_image')
# async def up_image(file: UploadFile = File(...)):
#     file_object = file.file
#     # create empty file to copy the file_object to
#     upload_folder = open(os.path.join('./static/images', file.filename), 'wb+')
#     shutil.copyfileobj(file_object, upload_folder)
#     upload_folder.close()
#     return {"file_url": '/static/images/' + file.filename}