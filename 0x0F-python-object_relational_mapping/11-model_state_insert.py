#!/usr/bin/python3
""" script that adds the State object “Louisiana” to the database
 hbtn_0e_6_usa """


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
    state6 = State(id=6, name="Louisiana")
    session.add(state6)
    session.commit()
    print(f"{state6.id}")
    session.close()
