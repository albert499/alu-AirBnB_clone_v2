#!/usr/bin/python3
""" new class for sqlAlchemy """
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """Interacts with the MySQL database using SQLAlchemy ORM"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize the DBStorage engine and session"""
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")

        # Create the engine with the MySQL configuration
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)

        # If the environment is 'test', drop all the tables
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query all objects depending on the class name or return all objects
        Args:
            cls: class name or None
        Return:
            Dictionary with all queried objects
        """
        dic = {}
        if cls:
            if isinstance(cls, str):
                cls = eval(cls)
            query = self.__session.query(cls)
            for elem in query:
                key = "{}.{}".format(type(elem).__name__, elem.id)
                dic[key] = elem
        else:
            # If no class is specified, query for all objects in these tables
            lista = [State, City, User, Place, Review, Amenity]
            for clase in lista:
                query = self.__session.query(clase)
                for elem in query:
                    key = "{}.{}".format(type(elem).__name__, elem.id)
                    dic[key] = elem
        return dic

    def new(self, obj):
        """Add a new object to the current session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes to the current session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete an object from the current session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reload the database session and create all tables"""
        # Create all tables if they don't exist
        Base.metadata.create_all(self.__engine)
        # Bind the engine to the session and configure session maker
        sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
        # Use scoped_session to manage sessions
        Session = scoped_session(sec)
        self.__session = Session()

    def close(self):
        """Close and remove the current session"""
        # Use scoped_session's remove method to close the session
        self.__session.remove()

