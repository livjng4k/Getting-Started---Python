from __future__ import annotations

from typing import List, TYPE_CHECKING

from base import Base
from sqlalchemy import Column, String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relationship

if TYPE_CHECKING:
    from models.roles import Role
    from models.users import User


class Account(Base):
    __tablename__ = 'account'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String)
    password = Column(String)
    # user_id = Column(Integer, ForeignKey('user.id'))

    disable = Column(Boolean, default=False)

    roles: List[Role] = relationship('Role', secondary='account_role')  # 1 account - n roles
    # user: User = relationship('User', uselist=False, back_populate='account')  # 1 account - 1 user(profile)


def __repr__(self):
    return "<Account(username = '%d', password='%s', user='%s')>" % (self.username, self.password, self.user_id)
