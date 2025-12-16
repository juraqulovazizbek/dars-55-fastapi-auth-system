from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
)
from sqlalchemy.orm import relationship

from app.db.base import Base


class User(Base):
    __tablename__ = 'users'

    user_id = Column('id', Integer, primary_key=True)
    username = Column('username', String(length=100), unique=True, nullable=False)
    password = Column('password', String(length=255), nullable=False)
    role = Column('role', String(length=20), nullable=False, default='user') # admin, manager, teacher, user, ...

    create_at = Column('create_at', DateTime, default=datetime.now)
    updated_at = Column('updated_at', DateTime, default=datetime.now, onupdate=datetime.now)

    tokens = relationship('AuthToken', back_populates='user')

    def __str__(self):
        return self.username   

    def __repr__(self):
        return self.username
