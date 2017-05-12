"""Database setup for Amity"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

""" create table called Andelans"""


class People(Base):
    __tablename__ = "Andelans"
    Name = Column(String(250), primary_key=True, nullable=False)
    person_id = Column(Integer, autoincrement=True)
    Role = Column(String(250))
    Accomodation = Column(String(1), nullable=True)  # Only for fellows
    RoomAllocated = Column(String(250), nullable=True)  # Room allocated


"""create table called Amity"""


class Rooms(Base):
    __tablename__ = "Amity Rooms"
    Name = Column(String(250), primary_key=True, nullable=False)
    room_id = Column(Integer, autoincrement=True)
    Purpose = Column(String(250), nullable=False)
    Occupants = Column(String(250), nullable=True)


""" Create engine that stores data in local directory"""
engine = create_engine("sqlite:///Amity_database.db")

Base.metadata.create_all(engine)  # create tables in the engine
