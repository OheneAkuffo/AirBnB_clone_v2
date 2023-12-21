#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(60), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", cascade='all, delete', backref='states')
    else:
        @property
        def cities(self):
            """
                Getter method for cities
                Return: list of cities with state_id equal to self.id
            """
            from models import storage
            from models.city import City

            all_cities = storage.all(City).value()
            same_city = []
            if all_cities:
                for city in all_cities:
                    if city.id == self.id:
                        same_city.append(city)
            return same_city
