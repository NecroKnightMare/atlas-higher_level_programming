#!/usr/bin/python3
"""
lists all State objects containing the letter a from usa db
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def list_states_with_a(username, password, database):
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.like('%a%')).order_by(State.id.asc()).all()
    for state in states:
        print(f"{state.id}: {state.name}")
    
    session.close()

if __name__ == "__main__":
    list_states_with_a(sys.argv[1], sys.argv[2], sys.argv[3])
