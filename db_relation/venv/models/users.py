from __future__ import annotations
from base import Base
from typing import List
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING :
    from models.orders import Order

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)

    orders: List[Order] = relationship("Order", back_populates='user')

def __repr__(self):
    return "<User(user_id = '%d', name='%s')>" % (self.id, self.name)