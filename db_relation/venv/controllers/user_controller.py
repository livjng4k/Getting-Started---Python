from models.users import User
import sqlalchemy as db
from typing import List


def add_users(session: db.orm.ession.Session, users: List[User]):
    session.add_many(users)
