from __future__ import annotations
import sqlalchemy as db
from typing import List
from sqlalchemy.orm.session import Session
from models.products import Product
from dto.product import ProductUpdateDTO, ProductCreateDto

class ProductRepository(object):
    def __init__(self, session: db.orm.Session):
        self.session: db.orm.Session = session


    def get_product(self, product_id: int):
        return self.session.query(Product).filter(Product.id == product_id, Product.disable == False).first()


    def get_all(self):
        return self.session.query(Product).filter(Product.disable == False).all()


    def get_all_query(self):
        return self.session.query(Product).filter(Product.disable == False)


    def save_product(self, seller_id: int, product_new: ProductCreateDto):
        product: Product
        try:
            product = Product(name=product_new.name, price=product_new.price, description=product_new.description, producer_id=product_new.producer_id, seller_id=seller_id)
            self.session.add(product)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            print(e)

        return product


    def update_product(self, product_id: int, product_update: ProductUpdateDTO):
        try:
            product: Product
            product = self.get_product(product_id)
            if product:
                product.name = product_update.name
                product.price = product_update.price
                product.description = product_update.description
                self.session.add(product)
                self.session.commit()
        except Exception:
            self.session.rollback()
            return None

        return product.id


    def remove_product(self, product_id: int):
        try:
            product: Product
            product = self.get_product(product_id)
            if product:
                product.disable = True
                self.session.add(product)
                self.session.commit()
        except Exception:
            self.session.rollback()
            return False

        return True
