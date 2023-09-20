#!/usr/bin/python3
"""This module defines a class to manage sql database for  hbnb clone"""
import models
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.user import User


class DBStorage:
    """a DBStorage class using sqlalchemy to represents a sql storage engine
    Attributes:
        __engine: set to None
        __session: set to None

    """
    __engine = None
    __session = None

    def __init__(self):
        """Initialization of a sql DB storage"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(getenv('HBNB_MYSQL_USER'),
                                             getenv('HBNB_MYSQL_PWD'),
                                             getenv('HBNB_MYSQL_HOST'),
                                             getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query all objects on the current database session
        and return a dict
        """
        obj_dict = {}
        if cls is None:
            all_cls = (State, City, User)
            for cls in all_cls:
                for obj in self.__session.query(cls):
                    key = "{}.{}".format(cls.__class__.__name__, obj.id)
                    obj_dict[key] = obj
        else:
            for obj in self.__session.query(cls):
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                if key != '_sa_instance_state':
                    obj_dict[key] = obj
        if "_sa_instance_state" in obj_dict:
            del obj_dict["_sa_instance_state"]
        return obj_dict

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
