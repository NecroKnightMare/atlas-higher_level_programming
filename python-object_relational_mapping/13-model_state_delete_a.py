#!/usr/bin/python3
"""
deletes all State objects with a name with the leeter from usa db.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def delete_states_with_a(username, password, database):
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')
    Session = sessionmaker(bind=engine)
    session = Session()

    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()
    for state in states_to_delete:
        session.delete(state)
    session.commit()

    session.close()

if __name__ == "__main__":
    delete_states_with_a(sys.argv[1], sys.argv[2], sys.argv[3])
