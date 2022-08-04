#!/usr/bin/python3
""" script that adds the State object “Louisiana” to the database
 hbtn_0e_6_usa """


import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session, sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    add_first = City(name="San Francisco", state=State(name="California"))
    session.add(add_first)
    session.commit()
    session.close()
