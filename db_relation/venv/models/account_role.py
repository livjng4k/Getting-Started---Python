from __future__ import annotations
from base import Base
from sqlalchemy import Column, Boolean, ForeignKey, Integer


class AccountRole(Base):
    __tablename__ = 'account_role'

    account_id = Column(Integer, ForeignKey('account.id'), primary_key=True)
    role_id = Column(Integer, ForeignKey('role.id'), primary_key=True)

    disable = Column(Boolean, default=False)

