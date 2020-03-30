#!/usr/bin/python3
# create class state
import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
