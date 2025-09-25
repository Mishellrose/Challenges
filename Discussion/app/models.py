from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base=declarative_base()

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True,nullable=False)
    title = Column(String(255), nullable=False)
    content = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"),nullable=False)
    owner=relationship("User")  

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True,nullable=False)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)


class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True,nullable=False)
    content = Column(String, nullable=False)
    post_id = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"),nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"),nullable=False)


class Vote(Base):
    __tablename__='votes'
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"),nullable=False)
    post_id = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"),nullable=False)


class Admin(Base):
    __tablename__='admins'
    id = Column(Integer, primary_key=True,nullable=False)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

