from __future__ import annotations
from base import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.producers import Producer
    from models.sellers import Seller


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False, default=1)
    description = Column(String, nullable=True)
    producer_id = Column(Integer, ForeignKey('producer.id'))
    seller_id = Column(Integer, ForeignKey('seller.id'))

    disable = Column(Boolean, default=False)

    producer: Producer = relationship('Producer', uselist=False, back_populates='products')
    seller: Seller = relationship('Seller', uselist=False, back_populates='products')


def __repr__(self):
    return "<Product(product_id = '%d', product_name='%s')>" % (self.id, self.name)
