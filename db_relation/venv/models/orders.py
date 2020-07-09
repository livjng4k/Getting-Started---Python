from __future__ import annotations
from base import Base
from typing import List
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING :
    from models.products import Product
    from models.users import User

class Order(Base):
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String, ForeignKey('user.id'))
    # order_checkout = Column(Integer)

    products: List[Product] = relationship("Product", secondary="order_detail")
    user: User = relationship("User", uselist=False, back_populates='orders')

def __repr__(self):
    return "<Order(order_id = '%d', user_id='%s')>" % (self.id, self.user_id)