from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime
)
from sqlalchemy.orm import relationship

from app.db.base import Base


class AuthToken(Base):
    __tablename__ = 'tokens'

    token_id = Column('id', Integer, primary_key=True)
    token = Column('token', String(length=128), unique=True, nullable=False)
    expires_date = Column('expires_date', DateTime)
    user_id = Column('user_id', ForeignKey('users.id', ondelete='CASCADE'))

    create_at = Column('create_at', DateTime, default=datetime.now)
    updated_at = Column('updated_at', DateTime, default=datetime.now, onupdate=datetime.now)

    user = relationship('User', back_populates='tokens')

    def __str__(self):
        return self.username   

    def __repr__(self):
        return self.username
