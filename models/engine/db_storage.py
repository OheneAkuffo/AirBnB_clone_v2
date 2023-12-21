#!/usr/bin/python3
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv
from urllib.parse import quote
classes = {'State': State, 'City': City,
           'User': User, 'Place': Place,
           'Review': Review, 'Amenity': Amenity}


class DBStorage:
    """
        Class the defines the mysql data storage
    """

    __engine = None
    __session = None

    def __init__(self):
        """
        Create the database engine.
        Drop all table in the database if environment
        variable HBNB_ENV is equal to test.
        """

        self.__engine = create_engine(
                "mysql+mysqldb://{}:{}@{}:3306/{}".
                format(getenv('HBNB_MYSQL_USER'),
                       quote(getenv('HBNB_MYSQL_PWD')),
                       getenv('HBNB_MYSQL_HOST'),
                       getenv('HBNB_MYSQL_DB')),
                pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
            Query and return all objects by class/generally
            Return: dictionary (<class-name>.<object-id>: <obj>)
        """
        obj_dict = {}

        if cls:
            for row in self.__session.query(cls).all():
                obj_dict.update({'{}.{}'.
                                format(type(cls).__name__, row.id): row})
        else:
            for key, val in classes.items():
                for row in self.__session.query(val):
                    obj_dict.update({'{}.{}'.
                                    format(val.__name__, row.id): row})
        return obj_dict

    def new(self, obj):
        """
            Add a new object to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """
            Save the current objects in the session to database
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
            Delete from current database session obj if not None
        """
        obj_cls = classes[type(obj).__name__]

        if obj:
            self.__session.query(obj_cls).filter(
                    obj_cls.id == obj.id).delete()

    def reload(self):
        """
            Create all tables.
            Create the current database session
        """
        Session = sessionmaker(
                bind=self.__engine, expire_on_commit=False)
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(Session)

    def close(self):
        """
            Close the session
        """
        self.__session.remove()
