#!/usr/bin/python3
""" script that prints the first State object from database hbtn_0e_6_usa """


import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session, sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    city = session.query(State).order_by(State.id).first()
    if city is None:
        print("Nothing")
    else:
        print(f"{city.id}: {city.name}")
    session.close()
