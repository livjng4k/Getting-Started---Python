from __future__ import annotations
from base import Base
from typing import List
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String,nullable=False)
    price = Column(Integer,nullable=False)
    description = Column(String, nullable=True)


def __repr__(self):
    return "<Product(product_id = '%d', product_name='%s')>" % (self.id, self.name)