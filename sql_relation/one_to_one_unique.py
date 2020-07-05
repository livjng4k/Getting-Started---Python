from __future__ import annotations
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
import sqlalchemy as db
from base import Base


class Student(Base):
    __tablename__ = 'students'

    student_id = Column(Integer, primary_key=True)
    name = Column(String)
    library_card: LibraryCard = relationship("LibraryCard", uselist=False, back_populates="student")


class LibraryCard(Base):
    __tablename__ = 'library_card'
    card_id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.student_id'), unique=True, nullable=False)
    student: Student = relationship("Student", back_populates="library_card")


def gen_student_enry(session: db.orm.session.Session):
    student1 = Student(student_id=1, name="Student 1")
    student2 = Student(student_id=2, name="Student 2")
    session.add_all([student1, student2])
    session.commit()


def gen_card_entry(session: db.orm.session.Session):
    card1 = LibraryCard(card_id=1, student_id=1)
    card2 = LibraryCard(card_id=2, student_id=2)
    session.add_all([card1, card2])
    session.commit()


def add_new_card_for_student(session: db.orm.session.Session):
    student: Student = session.query(Student).filter(Student.student_id == 1).first()
    if student:
        card = LibraryCard(card_id=3, student_id=1)
        student.library_card = card
        session.commit()


    student: Student = session.query(Student).filter(Student.student_id == 1).first()
    if student:
        card = LibraryCard(card_id=4, student_id=1)
        student.library_card = card
        session.commit()



def connect():
    engine = db.create_engine('sqlite:///example_one_to_one_unique.db', echo = True) #set echo = Tru to see sql log
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

    gen_student_enry(session)
    gen_card_entry(session)
    add_new_card_for_student(session)


    session.close()


if __name__ == "__main__":
    main()