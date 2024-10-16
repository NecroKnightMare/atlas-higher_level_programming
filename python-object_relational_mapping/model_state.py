#!/usr/bin/python3
"""
state class
"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
    State class that links to the MySQL table states
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    from sqlalchemy.orm import sessionmaker
    engine = create_engine('mysql+mysqldb://root:root@localhost:3306/hbtn_0e_0_usa')
    Base.metadata.create_all(engine)
