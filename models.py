# models.py
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Server(Base):
    __tablename__ = "server"
    id = Column(Integer, primary_key=True, index=True)
    server_name = Column(String, index=True)
    port = Column(Integer)
    # ...

class Auth(Base):
    __tablename__ = "auth"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    password = Column(String)
    accepted = Column(Boolean, default=False)
    # ...

class Log(Base):
    __tablename__ = "log"
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime)
    message = Column(String)
    # ...