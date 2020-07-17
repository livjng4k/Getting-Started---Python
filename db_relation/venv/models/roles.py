from __future__ import annotations
from base import Base
from sqlalchemy import Column, String, Boolean, Integer


class Role(Base):
    __tablename__ = 'role'

    id = Column(Integer, primary_key=True, autoincrement=True)
    role = Column(String)

    disable = Column(Boolean, default=False)


    def __repr__(self):
        return "<Role(id = '%d', role='%s')>" % (self.id, self.role)