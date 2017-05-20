"""Database setup for Amity"""
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()


class People(Base):
    __tablename__ = "Andelans"
    Name = Column(String(250), primary_key=True, nullable=False)
    Role = Column(String(250))
    RoomAllocated = Column(String(250), nullable=True)  # Room allocated


class Rooms(Base):
    __tablename__ = "Amity Rooms"
    Name = Column(String(250), primary_key=True, nullable=False)
    Purpose = Column(String(250), nullable=False)
    Occupants = Column(String(250), nullable=True)


# Create engine that stores data in local directory"""
engine = create_engine("sqlite:///Amity_database.db")

Base.metadata.create_all(engine)  # create tables in the engine
