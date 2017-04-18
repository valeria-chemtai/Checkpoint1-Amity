"""Database setup for Amity"""
from sqlalchemy import Column, Integer, String,
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

""" create table called Andelans"""


class PeopleTable(Base):
    __tablename__ = "Andelans"
    Name = Column(String(250), nullable=False)
    person_id = Column(Integer, primary_key=True, autoincrement=True)
    Accomodation = Column(String(1), nullable=True)  # Only for fellows
    Room_allocated = Column(String(250), nullable=True)  # Room allocated


"""create table called Amity"""


class RoomsTable(Base):
    __tablename__ = "Amity"
    Name = Column(String(250), nullable=False)
    room_id = Column(Integer, primary_key=True, autoincrement=True)
    # Column for Living Space or Office Space
    purpose = Column(String(250), nullable=False)
    # Column for Number of occupants in the room
    occupants = Column(Integer, nullable=True)


""" Create engine that stores data in local directory"""
engine = create_engine("sqlite:///Amity_database.db")

Base.metadata.create_all(engine)  # create tables in the engine
