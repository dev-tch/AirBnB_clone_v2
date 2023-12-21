"""
Define storage engine using MySQL database
"""
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm.session import sessionmaker, Session
from os import getenv

mapping_class = {'State': State, 'City': City, 'User': User}


class DBStorage:
    """
    This class manages MySQL storage using SQLAlchemy

    Attributes:
        ___engine: engine object
        __session: session object
    """
    __engine = None
    __session = None

    def __init__(self):
        """Create SQLAlchemy engine"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'.
                                      format(getenv('HBNB_MYSQL_USER'),
                                             getenv('HBNB_MYSQL_PWD'),
                                             getenv('HBNB_MYSQL_HOST'),
                                             getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        """drop tables if test environment"""
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query all objects of the given class."""
        if cls is None:
            objs = []
            for class_key, class_val in mapping_class.items():
                objs.extend(self.__session.query(class_val).all())
        else:
            if isinstance(cls, str):
                cls = eval(cls)
            objs = self.__session.query(cls).all()
        return {"{}.{}".format(type(o).__name__, o.id): o for o in objs}

    def new(self, obj):
        """Add object to current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from database session"""
        if obj:
            """determine class from obj"""
            cls_name = mapping_class[type(obj).__name__]

            """ query class table and delete """
            self.__session.query(cls_name).\
                filter(cls_name.id == obj.id).delete()

    def reload(self):
        """Create database session"""
        Base.metadata.create_all(self.__engine)
        """ create db tables"""
        session = sessionmaker(bind=self.__engine,
                               expire_on_commit=False)

        self.__session = scoped_session(session)

    def close(self):
        """Close scoped session"""
        self.__session.remove()
