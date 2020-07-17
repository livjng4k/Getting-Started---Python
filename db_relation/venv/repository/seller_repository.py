from __future__ import annotations
import sqlalchemy as db
from typing import List
from sqlalchemy.orm.session import Session
from models.sellers import Seller
from models.products import Product
from dto.seller import SellerCreateDto, SellerDetailDto
from dto.product import SellerCreateProductDto

class SellerRepository(object):
    def __init__(self, session: db.orm.Session):
        self.session: db.orm.Session = session


    def get_seller(self, seller_id: int):
        return self.session.query(Seller).filter(Seller.id == seller_id, Seller.disable == False).first()


    def get_all(self):
        return self.session.query(Seller).filter(Seller.disable == False).all()


    def save_seller(self, seller_new: SellerCreateDto):
        seller: Seller
        try:
            seller = Seller(name=seller_new.name, description=seller_new.description, logo=seller_new.logo, address=seller_new.address)

            self.session.add(seller)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            print(e)
            return None

        return seller


    def update_seller(self, seller_update: SellerDetailDto):
        seller: Seller
        try:
            seller = self.get_seller(seller_update.id)
            if seller:
                seller.name = seller_update.name
                seller.description = seller_update.description
                seller.logo = seller_update.logo
                seller.address = seller_update.address

                self.session.add(seller)
                self.session.commit()
        except Exception:
            self.session.rollback()
            return None

        return seller


    def remove_seller(self, seller_id: int):
        try:
            seller: Seller
            seller = self.get_seller(seller_id)
            if seller:
                seller.disable = True

                self.session.add(seller)
                self.session.commit()
        except Exception:
            self.session.rollback()
            return None

        return True


    def get_all_product(self, seller_id: int):
        seller: Seller
        seller = self.get_seller(seller_id)
        if seller is not None:
            return seller.products
        else:
            return None

