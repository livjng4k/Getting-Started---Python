from __future__ import annotations
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

session: db.orm.session = None

def get_session():
    global session
    if session is None:
        engine = db.create_engine('sqlite:///example_db.db', echo=False)
        Base.metadata.create_all(engine)
        Session: db.orm.session.sessionmaker = sessionmaker(bind=engine)
        sess: db.orm.Session = Session()
        session = sess
        session.execute("PRAGMA foreign_keys = 1")

    return session
