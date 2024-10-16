#!/usr/bin/python3
"""
prints state object with the name passed as an argument from usa db
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def fetch_state_by_name(username, password, database, state_name):
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == state_name).first()
    if state:
        print(f"{state.id}")
    else:
        print("Not found")
    
    session.close()

if __name__ == "__main__":
    fetch_state_by_name(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
