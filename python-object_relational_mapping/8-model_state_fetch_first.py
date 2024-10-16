#!/usr/bin/python3
"""
prints the first State object from usa db
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def print_first_state(username, password, database):
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')
    Session = sessionmaker(bind=engine)
    session = Session()

    first_state = session.query(State).order_by(State.id).first()
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")
    
    session.close()

if __name__ == "__main__":
    print_first_state(sys.argv[1], sys.argv[2], sys.argv[3])
