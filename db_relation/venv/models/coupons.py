from __future__ import annotations
import datetime
from base import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime


class Coupon(Base):
    __tablename__ = 'coupon'

    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String)
    description = Column(String, nullable=True)
    dateCreated = Column(DateTime, default=datetime.datetime.now())
    dateExpired = Column(DateTime, nullable=True, default=None)
    #
    percent = Column(Integer, nullable=True)  # percent to discount on orders
    maxDiscount = Column(Integer, nullable=True)  # max amount of money to discount
    minVolume = Column(Integer, nullable=True)  # min value of the order to use coupon

    disable = Column(Boolean, default=False)


def __repr__(self):
    return "<Coupon(code = '%d')>" % self.code
