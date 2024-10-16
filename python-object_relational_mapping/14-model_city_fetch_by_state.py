#!/usr/bin/python3
"""
prints all City objects from usa db

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

def fetch_cities_by_state(username, password, database):
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).join(State, City.state_id == State.id).order_by(City.id.asc()).all()
    for city in cities:
        print(f"{city.state.name}: ({city.id}) {city.name}")

    session.close()

if __name__ == "__main__":
    fetch_cities_by_state(sys.argv[1], sys.argv[2], sys.argv[3])
"""
"""

if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from model_city import City

    # Connect to the database
    engine = create_engine(f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Fetch all states and their associated cities
    states_with_cities = session.query(State).join(City).order_by(City.id).all()

    # Print the results
    for state in states_with_cities:
        print(f"{state.name}:")
        for city in state.cities:
            print(f"    ({city.id}) {city.name}")

    # Close the session
    session.close()

