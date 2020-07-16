from __future__ import annotations
import sqlalchemy as db
from sqlalchemy.orm.session import Session
from models.roles import Role

class RoleRepository(object):
    def __init__(self, session: db.orm.Session):
        self.session: db.orm.Session = session
        for r in ["ADMIN", "CUSTOMER", "SELLER"]:
            asd = self.get_role_by_name(r)
            if not asd:
                try:
                    self.session.add(Role(role=r))
                    self.session.commit()
                except Exception as e:
                    print(e)
                    self.session.rollback()


    def get_role_by_id(self, role_id: int):
        return self.session.query(Role).filter(Role.id == role_id, Role.disable == False).first()


    def get_role_by_name(self, role_name: str):
        return self.session.query(Role).filter(Role.role == role_name, Role.disable == False).first()

