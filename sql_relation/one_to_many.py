from __future__ import annotations
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
import sqlalchemy as db
from base import Base
from typing import List

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    name = Column(String)

    products: List[Product] = relationship("Product", back_populates="user")
    #products = relationship("Product", backref="user")

    def __repr__(self):
        return "<User(user_id = '%d', name='%s')>" % (self.user_id, self.name)


class Product(Base):
    __tablename__ = 'products'

    product_id = Column(Integer, primary_key=True)
    name = Column(String)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    user: User = relationship("User", back_populates="products")

    def __repr__(self):
        return "<Product(id = '%d', name='%s')>" % (self.product_id, self.name)


def gen_user_entry(session: db.orm.session.Session):
    user1 = User(user_id=1, name="User 1")
    user2 = User(user_id=2, name="User 2")

    session.add(user1)
    session.add(user2)
    session.commit()


def gen_product_entry(session: db.orm.session.Session):
    product1 = Product(product_id=1, name="Product 1", user_id=1)
    product2 = Product(product_id=2, name="Product 2", user_id=1)
    product3 = Product(product_id=3, name="Product 3", user_id=2)
    product4 = Product(product_id=4, name="Product 4", user_id=2)

    session.add_all([product1, product2, product3, product4])
    session.commit()


def get_all_users(session: db.orm.Session):
    print()
    print("get_all_users:")
    users = session.query(User).all()
    for u in users:
        print(u)


def get_all_product(session: db.orm.Session):
    print()
    print("get_all_product:")
    products = session.query(Product).all()
    for p in products:
        print(p)


def get_user_by_id(session: db.orm.session, id: int):
    print()
    print("get_user_by_id: id = %d" % id)
    users = session.query(User).filter(User.user_id == id)
    for u in users:
        print(u)


def get_product_by_user_id_old(session: db.orm.session, id: int):
    print()
    print("get_product_by_user_id_old: user_id = %d" % id)
    products = session.query(Product).filter(Product.user_id == id)
    for p in products:
        print(p)


def get_product_by_user_id_new(session: db.orm.session, id: int):
    print()
    print("get_product_by_user_id_new: user_id = %d" % id)
    users = session.query(User).filter(User.user_id == id)

    u: User
    for u in users:
        print(u.name, u.products)


def get_user_by_product_id_old(session: db.orm.session, product_id: int):
    print()
    print("get_user_by_product_id_old: product_id = %d" % product_id)
    products = session.query(Product).filter(Product.product_id == product_id)

    p: Product
    for p in products:
        users = session.query(User).filter(User.user_id == p.user_id)
        for u in users:
            print(u)


def get_user_by_product_id_new(session: db.orm.session, product_id: int):
    print()
    print("get_user_by_product_id_new: product_id = %d" % product_id)
    products = session.query(Product).filter(Product.product_id == product_id)

    p: Product
    for p in products:
        print(p.user)


def get_users_and_products(session: db.orm.session):
    print()
    print("get_users_and_products:")

    for u, p in session.query(User, Product).filter(User.user_id == Product.user_id).all():
        print(u)
        print(p)

    all = session.query(User, Product).filter(User.user_id == Product.user_id).all()
    print(all)


def add_new_product_to_user(session: db.orm.session, user_id: int):
    print()
    print("add_new_product_to_user:")

    user: User = session.query(User).filter(User.user_id == user_id).first()
    if user:
        product = Product(product_id=5, name="Product 5")
        user.products.append(product)
        print(user.products)
        session.commit()


def get_user_by_user_id(session: db.orm.Session, user_id: int):
    return session.query(User).filter(User.user_id == user_id).first()


def add_new_product_to_user_2(session: db.orm.Session, id: int):
    user = get_user_by_user_id(session, id)
    product = Product(product_id=6, name="Product 6", user_id=id)
    session.add(product)
    session.commit()
    print(user.products)


def connect():
    engine = db.create_engine('sqlite:///example_one_to_many.db', echo = False) #set echo = Tru to see sql log
    return engine

engine = connect()
Base.metadata.create_all(engine)


def main():
    Session: db.orm.session.sessionmaker = sessionmaker(bind=engine)
    session: db.orm.Session = Session()
    session.execute("PRAGMA foreign_keys = 1")
    session.commit()

    result = session.execute("PRAGMA foreign_keys")
    print(result.fetchall())
    session.commit()

    #gen_user_entry(session)
    #gen_product_entry(session)
    #get_all_users(session)
    #get_all_product(session)
    #get_user_by_id(session, 1)
    #get_product_by_user_id_old(session, 1)
    #get_product_by_user_id_new(session, 1)
    #get_user_by_product_id_old(session, 3)
    #get_user_by_product_id_new(session, 3)
    #get_users_and_products(session)
    #add_new_product_to_user(session, 1)
    add_new_product_to_user_2(session, 1)

    session.close()


if __name__ == "__main__":
    main()