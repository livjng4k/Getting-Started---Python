from __future__ import annotations
from base import Base
from sqlalchemy import Column, Integer, String, Boolean


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Integer, nullable=True)

    disable = Column(Boolean, default=False)


def __repr__(self):
    return "<Product(product_id = '%d', product_name='%s')>" % (self.id, self.name)
