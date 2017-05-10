"""Class Amity is the controller of the app using
the Models Views Controller concept i.e. MVC"""
import os
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from Models.person import Person, Fellow, Staff
from Models.room import Room, Office, LivingSpace
from Models.database import People, Rooms

"""Initiate link to database for storage and retrival of data"""
engine = create_engine("sqlite:///Amity_database.db")
Base = declarative_base()
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


class Amity(object):

    def __init__(self):
        self.room_list = []
        self.office_list = []
        self.living_space_list = []
        self.allocated = []
        self.unallocated = []

    """ method for creating rooms in Amity """

    def create_room(self, room_name, purpose):
        if (isinstance(room_name, str) and isinstance(purpose, str)):
            if [room for room in self.room_list
                    if room_name == room.room_name]:
                print("{} Exists in Amity.".format(room_name))
                return "{} Exists in Amity.".format(room_name)
            else:
                if purpose == "OFFICE" or purpose == "office":
                    room = Office(room_name)
                    self.office_list.append(room)
                    self.room_list.append(room)
                    print("{} {} created".format(room.room_name, room.purpose))
                    return "Room Created"
                elif purpose == "LIVINGSPACE" or purpose == "livingspace":
                    room = LivingSpace(room_name)
                    self.living_space_list.append(room)
                    self.room_list.append(room)
                    print("{} {} created".format(room.room_name, room.purpose))
                    return "Room Created"
                else:
                    print("{} is not a valid room type.".format(purpose))
        else:
            print("Invalid Room Name")
            return "Invalid Room Name"

    """ method for adding a fellow/staff to amity database """

    def add_person(self, first_name, second_name, role, wants_accomodation):
        if (isinstance(first_name, str) and isinstance(second_name, str)):
            person_name = first_name + " " + second_name
            allocated = [allocated for allocated in self.allocated
                         if person_name == allocated.person_name]
            unallocated = [unallocated for unallocated in self.unallocated
                           if person_name == unallocated.person_name]
            person = allocated or unallocated
            if person:
                print("{} Exists in Amity.".format(person_name))
                return "{} Exists in Amity.".format(person_name)

            else:
                if role == "FELLOW" and wants_accomodation == "N":
                    person = Fellow(person_name, wants_accomodation)
                    self.allocate_office(person)
                    return "Fellow Added"
                elif role == "FELLOW" and wants_accomodation == "Y":
                    person = Fellow(person_name, wants_accomodation)
                    self.allocate_office(person)
                    self.allocate_living_space(person)
                    return "Fellow Added and LIvingSpace Allocated"
                elif role == "STAFF":
                    person = Staff(person_name)
                    self.allocate_office(person)
                    return "Staff Added"
                else:
                    print("{} is not a valid room type.".format(role))

        else:
            print("Invalid Person Name")
            return "Invalid Person Name"

    """allocate_office is a method used for allocation of
    office to both staff and fellows"""

    def allocate_office(self, person):
        if self.office_list:
            office = random.choice(self.office_list)
            if len(office.occupants) < 6:
                office.occupants.append(person)
                self.allocated.append(person)
                print("{} allocated office {}".format(person.person_name,
                                                      office.room_name))
            else:
                print("Room full")
        else:
            self.unallocated.append(person)
            print("No Office available now, {} placed in waiting list ".
                  format(person.person_name))

    def allocate_living_space(self, person):
        if self.living_space_list:
            living = random.choice(self.living_space_list)
            if len(living.occupants) < 4:
                living.occupants.append(person)
                print("and allocated livingspace {}".format(living.room_name))
            else:
                print("Room Full")

        else:
            print(
                "No living space available now, {} placed in waiting list ".
                format(person))

    """ method to reallocate a person to another room """

    def reallocate_person(self, first_name, second_name, room_name):
        person_name = first_name + " " + second_name
        allocated = [allocated for allocated in self.allocated if
                     person_name == allocated.person_name]
        unallocated = [unallocated for unallocated in self.unallocated if
                       person_name == unallocated.person_name]
        room = [room for room in self.room_list if room_name == room.room_name]
        person = allocated or unallocated
        if not person:
            print("Add {} to Amity first".format(person_name))
            return "Add {} to Amity first".format(person_name)
        elif not room:
            print("{} is not a room in Amity".format(room_name))
            return "{} is not a room in Amity".format(room_name)

        elif [occupant for occupant in room[0].occupants
                if person_name == occupant.person_name]:
            print("{} is already in {}".format(person_name, room[0].room_name))
            return "{} is already in {}".format(person_name, room[0].room_name)

        elif room[0].purpose == "living_space" and person[0].role == "Staff":
            print("{} is a living space. Staff can only be allocated offices"
                  .format(room[0].room_name))
            return "Staff cannot be allocated living space"

        elif (room[0].purpose == "office" and len(room[0].occupants) == 6):
            print("{} is full.".format(room[0].room_name))
            return"Room is Full"

        elif (room[0].purpose == "living_space" and len(room[0].occupants) == 4):
            print("{} is full.".format(room[0].room_name))
            return"Room is Full"

        elif unallocated:
            room[0].occupants.append(person[0])
            print("{} moved from waiting list to {}".format(
                person[0].person_name, room[0].room_name))
            return "Moved to {}".format(room[0].room_name)
        else:
            old_room = [room for room in self.room_list if person[0] in room.occupants]
            room[0].occupants.append(person[0])
            old_room[0].occupants.remove(person[0])
            person[0].old_room = room[0].room_name
            print("{} was moved from {} to {}".format(
                person[0].person_name, old_room[0].room_name, room[0].room_name))
            return "Reallocated Successfully"

    """ method to add people to rooms from a text file """

    def load_people(self, filename):
        try:
            with open(filename, 'r') as f:
                people = f.readlines()
            for person in people:
                params = person.split()
                self.add_person(params[0], params[1], params[2], params[3])
            print("People Successfully Loaded")
            return "People Successfully Loaded"
        except FileNotFoundError:
            print("File not found in the path specified")
            return "File not found"

    """ method to print a list of allocations on screen
     with option to store in a txt file """

    def print_allocations(self, filename):
        pass

    """ method to print a list of unallocated people in screen
     with option to store in a text file """

    def print_unallocated(self, filename):
        if len(self.unallocated) == 0:
            print("No Member in Unallocated")
            return "No Member in Unallocated"
        else:
            for person in self.unallocated:
                person_name = person.person_name
                print(person_name)
        if filename:
            with open(filename, 'w') as f:
                f.write(person_name)
            print("Data Saved to Text File")
            return "Data Saved to Text File"
        return "Unallocated Printed"

    """ method to print room and all people allocated to that room."""

    def print_room(self, room_name):
        room = [room for room in self.room_list if room_name == room.room_name]
        if room:
            room = room[0]
            print("{}".format(room.room_name))
            for person in room.occupants:
                print(person.person_name)
            return "Print room successful"
        else:
            print("{} does not exist in Amity".format(room_name))
            return "Room does not exist"

    """ method to save all data in the app into SQLite database """

    def save_state(self, database_name):
        for person in self.allocated + self.unallocated:
            rooms_allocated = " "
            for room in self.room_list:
                if person in room.occupants:
                    rooms_allocated = room.room_name + "  "
            person = People(Name=person.person_name, Role=person.role,
                            Accomodation=person.wants_accomodation,
                            RoomAllocated=rooms_allocated)
            session.add(person)
        for room in self.room_list:
            people = " "
            for occupant in room.occupants:
                people += occupant.person_name + "  "
            room = Rooms(Name=room.room_name,
                         Purpose=room.purpose, Occupants=people)
            session.add(room)
        session.commit()

    """ method to load data from database into the app """

    def load_state(self, database_name):
        """Load room data"""
        for room_name, purpose, occupants in session.query(Rooms.Name, Rooms.Purpose, Rooms.Occupants):
            individuals = occupants.split("  ")
            individuals.remove("")
            if purpose == "office":
                room = Office(room_name)
                for individual in individuals:
                    person = Person(individual)
                    room.occupants.append(person)
                self.office_list.append(room)
                self.room_list.append(room)
            elif purpose == "living_space":
                room = LivingSpace(room_name)
                for individual in individuals:
                    person = Person(individual)
                    room.occupants.append(person)
                self.living_space_list.append(room)
                self.room_list.append(room)
        for person_name, role, wants_accomodation, rooms_allocated in session.query(People.Name, People.Role, People.Accomodation, People.RoomAllocated):
            if role == "FELLOW":
                person = Fellow(person_name)
                if rooms_allocated:
                    self.allocated.append(person)
                else:
                    self.unallocated.append(person)
            else:
                person = Staff(person_name)
                if rooms_allocated:
                    self.allocated.append(person)
                else:
                    self.unallocated.append(person)
