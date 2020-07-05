from __future__ import annotations
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
import sqlalchemy as db
from base import Base
from typing import List

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    name = Column(String)
    orders: List[Order] = relationship("Order", back_populates="user")

    def __repr__(self):
        return "<User(id = '%d', name='%s')>" % (self.user_id, self.name)

class OrderDetail(Base):
    __tablename__ = "order_details"

    order_id = Column(Integer, ForeignKey('orders.order_id'), primary_key=True)
    product_id = Column(Integer, ForeignKey('products.product_id'), primary_key=True)


class Order(Base):
    __tablename__ = 'orders'

    order_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))

    user: User = relationship("User", back_populates="orders")

    products: List[Product] = relationship(
        "Product",
        secondary="order_details",
        back_populates="orders")

    def __repr__(self):
        return "<Order(id = '%d', user_id='%d', products='%s')>" % (self.order_id, self.user_id, self.products)

class Product(Base):
    __tablename__ = 'products'

    product_id = Column(Integer, primary_key=True)
    name = Column(String)
    orders = relationship(
        "Order",
        secondary="order_details",
        back_populates="products")

    def __repr__(self):
        return "<Product(id = '%d', name='%s')>" % (self.product_id, self.name)


def gen_entry(session: db.orm.session.Session):
    # gen users and orders
    user1 = User(user_id=1, name="User 1")
    user2 = User(user_id=2, name="User 2")
    order1 = Order(order_id=1)
    user1.orders.append(order1)
    order2 = Order(order_id=2)
    user2.orders.append(order2)
    session.add_all([user1, user2])

    # gen products
    product1 = Product(product_id=1, name="Product 1")
    product2 = Product(product_id=2, name="Product 2")
    product3 = Product(product_id=3, name="Product 3")
    product4 = Product(product_id=4, name="Product 4")
    session.add_all([product1, product2, product3, product4])

    # gen order details
    order_detail1_1 = OrderDetail(order_id=1, product_id=1)
    order_detail1_2 = OrderDetail(order_id=1, product_id=2)
    order_detail2_1 = OrderDetail(order_id=2, product_id=2)
    session.add_all([order_detail1_1, product2, order_detail1_2, order_detail2_1])
    session.commit()


def get_order_by_user_id(session: db.orm.Session, id: int):
    print()
    print("get_order_by_user_id: user_id = %d" % id)

    user: User = session.query(User).filter(User.user_id == id).first()
    if user:
        for order in user.orders:
            #print(order)
            for p in order.products:
                print(p.product_id, p.name, p.orders)

def connect():
    engine = db.create_engine('sqlite:///example_many_to_many.db', echo = False) #set echo = Tru to see sql log
    return engine

engine = connect()
Base.metadata.create_all(engine)

def add_new_order(session: db.orm.Session):
    order = Order(order_id=3, user_id=1)
    order_detail1 = OrderDetail(order_id=3, product_id=3)
    order_detail2 = OrderDetail(order_id=3, product_id=4)
    session.add_all([order, order_detail1, order_detail2])
    session.commit()

def get_all_products(session: db.orm.Session):
    products = session.query(Product).all()
    for p in products:
        print(p.product_id, p.name, p.orders)

def main():
    Session: db.orm.session.sessionmaker = sessionmaker(bind=engine)
    session: db.orm.Session = Session()
    session.execute("PRAGMA foreign_keys = 1")
    session.commit()

    #gen_entry(session)
    #get_order_by_user_id(session, 1)
    #get_order_by_user_id(session, 2)
    #add_new_order(session)
    get_all_products(session)
    session.close()


if __name__ == "__main__":
    main()