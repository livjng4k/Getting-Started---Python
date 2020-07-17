from __future__ import annotations

import datetime

from base import Base
from typing import List
from sqlalchemy import Column, Integer, String, Boolean, Date, DateTime
from sqlalchemy.orm import relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.orders import Order
    from models.accounts import Account


# User's profile
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, default=' ')
    dob = Column(Date, default=datetime.date.today())
    email = Column(String, default=' ')
    phone = Column(String, default=' ')
    avatar = Column(String, default=' ')
    dateCreated = Column(DateTime, default=datetime.datetime.now())

    disable = Column(Boolean, default=False)

    orders: List[Order] = relationship("Order", back_populates='user')
    # account: Account = relationship('Account', uselist=False, back_populates='user')


    def __repr__(self):
        return "<User(user_id = '%d', name='%s')>" % (self.id, self.name)
