from __future__ import annotations
import datetime
import sqlalchemy as db
from base import Base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import query

from models.users import User
from models.accounts import Account
from models.orders import Order
from models.products import Product
from models.coupons import Coupon
from models.roles import Role
from models.producers import Producer
from models.sellers import Seller
from models.account_role import AccountRole
from models.order_detail import OrderDetail


def connect():
    engine = db.create_engine('sqlite:///db_my_tiki.db', echo=False)
    return engine


engine = connect()
Base.metadata.create_all(engine)


def add_users(session: db.orm.session.Session):
    user1 = User(name="user 1")
    user2 = User(name="user 2")
    user3 = User(name="user 3")

    session.add_all([user1, user2, user3])


def add_accounts(session: db.orm.session.Session):
    account1 = Account(username="user1", password="123")
    account2 = Account(username="user2", password="123")
    account3 = Account(username="user3", password="123")

    session.add_all([account1, account2, account3])


def add_roles(session: db.orm.session.Session):
    role1 = Role(role="Customer")
    role2 = Role(role="Seller")
    role3 = Role(role="Admin")

    session.add_all([role1, role2, role3])


def add_to_product_users(session: db.orm.session.Session, user_id: int):
    oder1: Order = Order()
    oder2: Order = Order()
    oder3: Order = Order()
    oder4: Order = Order()
    oder5: Order = Order()

    user: User = session.query(User).filter(User.id == user_id).first()

    user.orders.append(oder1)
    user.orders.append(oder2)
    user.orders.append(oder3)
    user.orders.append(oder4)
    user.orders.append(oder5)


def get_all_order_by_user_id(session: db.orm.session.Session, user_id: int):
    user: User = session.query(User).filter(User.id == user_id).first()

    for o in user.orders:
        print(o)
        print("user info: ", o.user.id)


def add_to_product(session: db.orm.session.Session):
    p1 = Product(name="Iphone", price=20000, description="Product of Apple corp.")
    p2 = Product(name="SamSung", price=10000, description="Product of SamSung corp.")
    p3 = Product(name="Xiaomi", price=5000, description="Product of Xiaomi corp.")

    session.add_all([p1, p2, p3])


def add_product_order(session: db.orm.session.Session):
    p1 = Product(name="Iphone", price=20000, description="Product of Apple corp.")
    p2 = Product(name="SamSung", price=10000, description="Product of SamSung corp.")
    p3 = Product(name="Xiaomi", price=5000, description="Product of Xiaomi corp.")

    order_all = session.query(Order)

    o: Order
    for o in order_all:
        o.products.append(p1)
        o.products.append(p2)
        o.products.append(p3)


def add_producer(session: db.orm.session.Session):
    p1 = Producer(name="Apple", description="Apple products: Iphone...", logo="Aplle")
    p2 = Producer(name="Samsung", description="Samsung products: Galaxy...", logo="Samsung")

    session.add_all([p1, p2])


def add_seller(session: db.orm.session.Session):
    p1 = Seller(name="Apple Distributer 1", description="Apple products: Iphone...")
    p2 = Producer(name="Samsung Distributer 1", description="Samsung products: Galaxy...")
    p3 = Seller(name="Apple Distributer 2", description="Apple products: Iphone...")
    p4 = Producer(name="Samsung Distributer 2", description="Samsung products: Galaxy...")

    session.add_all([p1, p2, p3, p4])


def add_product_seller(session: db.orm.session.Session, seller_id: int):
    seller: Seller = session.query(Seller).filter(Seller.id == seller_id).first()

    if seller:
        seller.products.append(Product(name="Iphone", price=20000, description="Product of Apple corp."))
        seller.products.append(Product(name="SamSung", price=10000, description="Product of SamSung corp."))


def main():
    Session: db.orm.session.sessionmaker = sessionmaker(bind=engine)
    session: db.orm.Session = Session()
    session.execute("PRAGMA foreign_keys = 1")

    add_producer(session)
    add_seller(session)
    add_product_seller(session)

    session.commit()
    session.close()


if __name__ == "__main__":
    main()

