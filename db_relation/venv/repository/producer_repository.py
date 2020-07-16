from __future__ import annotations
import sqlalchemy as db
from typing import List
from sqlalchemy.orm.session import Session
from models.producers import Producer
from dto.producer import ProducerDTO

class ProducerRepository(object):
    def __init__(self, session: db.orm.Session):
        self.session: db.orm.Session = session


    def get_producer(self, producer_id: int):
        return self.session.query(Producer).filter(Producer.id == producer_id, Producer.disable == False).first()


    def get_all(self):
        return self.session.query(Producer).filter(Producer.disable == False).all()


    def get_all_query(self):
        return self.session.query(Producer).filter(Producer.disable == False)


    def save_producer(self, producer_new: ProducerDTO):
        producer: Producer
        try:
            producer = Producer(name=producer_new.name, description=producer_new.description, logo=producer_new.logo)
            self.session.add(producer)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            print(e)
            return None

        return producer


    def update_producer(self, Producer_id: int, producer_update: ProducerDTO):
        try:
            producer: Producer
            producer = self.get_Producer(Producer_id)
            if producer:
                producer.name = producer_update.name
                producer.price = producer_update.price
                producer.description = producer_update.description
                self.session.add(producer)
                self.session.commit()
        except Exception:
            self.session.rollback()
            return None

        return producer.id


    def remove_producer(self, producer_id: int):
        try:
            producer: Producer
            producer = self.get_producer(producer_id)
            if producer:
                producer.disable = True
                self.session.add(producer)
                self.session.commit()
        except Exception:
            self.session.rollback()
            return None

        return True
