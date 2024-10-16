#!/usr/bin/python3
"""
adds the State object "Louisiana" to usa db
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def add_state(username, password, database):
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
    print(new_state.id)
    
    session.close()

if __name__ == "__main__":
    add_state(sys.argv[1], sys.argv[2], sys.argv[3])
