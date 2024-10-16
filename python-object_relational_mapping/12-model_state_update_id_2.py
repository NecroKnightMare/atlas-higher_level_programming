#!/usr/bin/python3
"""
changes the name of a State object from usa db
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def update_state_name(username, password, database):
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')
    Session = sessionmaker(bind=engine)
    session = Session()

    state_to_update = session.query(State).filter(State.id == 2).first()
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()

    session.close()

if __name__ == "__main__":
    update_state_name(sys.argv[1], sys.argv[2], sys.argv[3])
