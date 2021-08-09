#!/usr/bin/python3
""" Print all City objects from the database """

if __name__ == "__main__":
    from sys import argv

    if len(argv) < 4:
        print("Error: this script requires 3 arguments")
        exit()

    from model_city import City
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}"
        .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()

    states = session.query(State, City).filter(City.state_id == State.id).all()

    for states, cities in states:
        print("{}: ({}) {}".format(states.name, cities.id, cities.name))

    session.close()
