from base import Base
from sqlalchemy import Column, Integer, ForeignKey


class OrderDetail(Base):
    __tablename__ = 'order_detail'

    order_id = Column(Integer, ForeignKey('order.id'), primary_key=True)
    product_id = Column(Integer, ForeignKey('product.id'), primary_key=True)
    amount = Column(Integer)
    price = Column(Integer)

