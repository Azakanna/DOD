from app.db.base_class import Base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)
