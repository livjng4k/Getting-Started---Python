from __future__ import annotations
from base import Base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from models.products import Product


class Seller(Base):
    __tablename__ = 'seller'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    logo = Column(String, nullable=True)
    address = Column(String, nullable=True)

    disable = Column(Boolean, default=False)

    products: List[Product] = relationship('Product', back_populates='seller')


def __repr__(self):
    return "<Seller(seller_id = '%d', seller_name='%s')>" % (self.id, self.name)
