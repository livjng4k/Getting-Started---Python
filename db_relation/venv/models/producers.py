from __future__ import annotations
from base import Base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from models.products import Product


class Producer(Base):
    __tablename__ = 'producer'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    logo = Column(String, nullable=False)

    disable = Column(Boolean, default=False)

    products: List[Product] = relationship('Product', back_populates='producer')


    def __repr__(self):
        return "<Producer(producer_id = '%d', producer_name='%s')>" % (self.id, self.name)

