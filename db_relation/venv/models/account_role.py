from __future__ import annotations
from base import Base
from sqlalchemy import Column, String, Boolean


class AccountRole(Base):
    __tablename__ = 'account_role'

    account_id = Column(String, primary_key=True)
    role_id = Column(String, primary_key=True)

    disable = Column(Boolean, default=False)


def __repr__(self):
    return "<Account(username = '%d', password='%s')>" % (self.username, self.password)