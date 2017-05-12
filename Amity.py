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
        self.rooms = []
        self.offices = []
        self.living_spaces = []
        self.allocated = []
        self.unallocated = []

    def create_room(self, room_name, purpose):
        """ method for creating rooms in Amity """
        if (isinstance(room_name, str) and isinstance(purpose, str)):
            if [room for room in self.rooms
                    if room_name.upper() == room.room_name.upper()]:
                print("{} Exists in Amity.".format(room_name.upper()))
                return "{} Exists in Amity.".format(room_name.upper())
            else:
                if purpose == "OFFICE" or purpose == "office":
                    room = Office(room_name.upper())
                    self.offices.append(room)
                    self.rooms.append(room)
                    print("{} {} created".format(room.room_name, room.purpose))
                    return "Room Created"
                elif purpose == "LIVINGSPACE" or purpose == "livingspace":
                    room = LivingSpace(room_name.upper())
                    self.living_spaces.append(room)
                    self.rooms.append(room)
                    print("{} {} created".format(room.room_name, room.purpose))
                    return "Room Created"
                else:
                    print("{} is not a valid room type.".format(purpose))
        else:
            print("Invalid Room Name")
            return "Invalid Room Name"

    def add_person(self, first_name, second_name, role, wants_accomodation):
        """ method for adding a fellow/staff to amity database """
        if (isinstance(first_name, str) and isinstance(second_name, str)):
            person_name = first_name.upper() + " " + second_name.upper()
            allocated = [allocated for allocated in self.allocated
                         if person_name.upper() == allocated.
                         person_name.upper()]
            unallocated = [unallocated for unallocated in self.unallocated
                           if person_name.upper() == unallocated.
                           person_name.upper()]
            person = allocated or unallocated
            if person:
                print("{} Exists in Amity.".format(person_name))
                return "{} Exists in Amity.".format(person_name)

            else:
                if role.upper() == "FELLOW" and wants_accomodation == "N":
                    person = Fellow(person_name, wants_accomodation)
                    self.allocate_office(person)
                    return "Fellow Added"
                elif role.upper() == "FELLOW" and wants_accomodation == "Y":
                    person = Fellow(person_name, wants_accomodation)
                    self.allocate_office(person)
                    self.allocate_living_space(person)
                    return "Fellow Added and LIvingSpace Allocated"
                elif role.upper() == "STAFF" and wants_accomodation == "N":
                    person = Staff(person_name)
                    self.allocate_office(person)
                    return "Staff Added"
                elif role.upper() == "STAFF" and wants_accomodation == "Y":
                    person = Staff(person_name)
                    self.allocate_office(person)
                    print("Staff Added and Allocated Office Only")
                    return "Staff Added and Allocated Office Only"
                else:
                    print("{} is not a valid room type.".format(role))

        else:
            print("Invalid Person Name")
            return "Invalid Person Name"

    def allocate_office(self, person):
        """allocate_office is a method used for allocation of
        office to both staff and fellows"""
        if self.offices:
            office = random.choice(self.offices)
            if len(office.occupants) < 6:
                office.occupants.append(person)
                self.allocated.append(person)
                print("{} allocated office {}".format(person.person_name,
                                                      office.room_name))
            else:
                print("{} Room full".format(office.room_name))
        else:
            self.unallocated.append(person)
            print("No Office available now, {} placed in waiting list ".
                  format(person.person_name))

    def allocate_living_space(self, person):
        if self.living_spaces:
            living = random.choice(self.living_spaces)
            if len(living.occupants) < 4:
                living.occupants.append(person)
                print("and allocated livingspace {}".format(living.room_name))
            else:
                print("{} Room Full".format(living.room_name))

        else:
            self.unallocated.append(person)
            print(
                "No living space available now, {} placed in waiting list ".
                format(person.person_name))

    def allocate_unallocated_office(self, person):
        if self.offices:
            office = random.choice(self.offices)
            if len(office.occupants) < 6:
                office.occupants.append(person[0])
                self.allocated.append(person[0])
                self.unallocated.remove(person[0])
                print("{} moved from waiting list to {}".
                      format(person[0].person_name, office.room_name))
                return "Now Allocated Office"
            else:
                print("Room Full Try Later")
                return "Room Full Try Later"
        else:
            print("No Offices Available Yet")
            return "No Offices Available Yet"

    def allocate_unallocated_livingspace(self, person):
        if self.living_spaces:
            living = random.choice(self.living_spaces)
            if len(living.occupants) < 4:
                living.occupants.append(person[0])
                self.allocated.append(person[0])
                self.unallocated.remove(person[0])
                print("{} moved from waiting list to {}".format(person[0].person_name, living.room_name))
                return "Fellow Now Allocated LivingSpace"
            else:
                print("Room Full Try Later")
                return "Room Full Try Later"
        else:
            print("No Livingspaces Available Yet")

    def allocate_unallocated(self, first_name, second_name):
        """Method to allocate unallocate members rooms"""
        person_name = first_name.upper() + " " + second_name.upper()
        person = [person for person in self.unallocated if
                  person_name.upper() == person.person_name.upper()]
        room = [room for room in self.rooms if person[0] in room.occupants]

        if not person:
            print("{} Not in Unallocated".format(person_name))
            return "{} Not in Unallocated".format(person_name)

        elif person and room:
            if room[0].purpose == "office":
                self.allocate_unallocated_livingspace(person)
            elif room[0].purpose == "living_space":
                self.allocate_unallocated_office(person)

        else:
            self.allocate_unallocated_office(person)

    def reallocate_person(self, first_name, second_name, room_name):
        """ method to reallocate a person to another room """
        person_name = first_name.upper() + " " + second_name.upper()
        allocated = [allocated for allocated in self.allocated if
                     person_name.upper() == allocated.person_name.upper()]
        unallocated = [unallocated for unallocated in self.unallocated if
                       person_name.upper() == unallocated.person_name.upper()]
        room = [room for room in self.rooms if room_name.upper() ==
                room.room_name.upper()]
        person = allocated
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

        elif (room[0].purpose == "office" and len(room[0].occupants) == 6):
            print("{} is full.".format(room[0].room_name))
            return"Room is Full"

        elif (room[0].purpose == "living_space" and
              len(room[0].occupants) == 4):
            print("{} is full.".format(room[0].room_name))
            return"Room is Full"

        else:
            old_room = [room for room in self.rooms if person[
                0] in room.occupants]
            if old_room[0].purpose == room[0].purpose:
                room[0].occupants.append(person[0])
                old_room[0].occupants.remove(person[0])
                person[0].old_room = room[0].room_name
                print("{} was moved from {} to {}".format(
                    person[0].person_name, old_room[0].room_name,
                    room[0].room_name))
                return "Reallocated Successfully"

            else:
                print("Can Only Reallocate to Room with Purpose as Current Room")
                return "Choose Appropriate Room Type"

    def load_people(self, filename):
        """ method to add people to rooms from a text file """

        try:
            with open(filename, 'r') as f:
                people = f.readlines()
            for person in people:
                params = person.split() + ["N"]
                self.add_person(params[0], params[1], params[2], params[3])
            print("People Successfully Loaded")
            return "People Successfully Loaded"

        except FileNotFoundError:
            print("File not found in the path specified")
            return "File not found"

    def print_allocations(self, filename):
        """ method to print a list of allocations on screen
        with option to store in a txt file """
        if not self.rooms:
            print("No Rooms to Show")
            return "No Rooms"
        output = " "
        for room in self.rooms:
            if len(room.occupants):
                output += room.room_name.upper() + '\n'
                output += "--" * 60 + '\n'
                for occupant in room.occupants:
                    output += occupant.person_name + ", "
                output += ("\n\n")
        print(output)

        if filename:
            with open(filename, 'w') as f:
                f.write(output)
            print("Allocations Printed to {}".format(filename))
            return "Allocations Printed to {}".format(filename)
        return "Successfully Printed Allocations"

    def print_unallocated(self, filename):
        """ method to print a list of unallocated people in screen
        with option to store in a text file """

        if not self.unallocated:
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

    def print_room(self, room_name):
        """ method to print room and all people allocated to that room."""
        room = [room for room in self.rooms if room_name.upper() ==
                room.room_name.upper()]
        if room:
            room = room[0]
            print("{}".format(room.room_name.upper()))
            for person in room.occupants:
                print(person.person_name)
            return "Print room successful"
        else:
            print("{} does not exist in Amity".format(room_name.upper()))
            return "Room does not exist"

    def save_state(self, database_name):
        """ method to save all data in the app into SQLite database """
        try:
            for person in self.allocated + self.unallocated:
                rooms_allocated = " "
                for room in self.rooms:
                    if person in room.occupants:
                        rooms_allocated = room.room_name + "  "
                person = People(Name=person.person_name, Role=person.role,
                                Accomodation=person.wants_accomodation,
                                RoomAllocated=rooms_allocated)
                session.add(person)
            for room in self.rooms:
                people = " "
                for occupant in room.occupants:
                    people += occupant.person_name + "  "
                room = Rooms(Name=room.room_name,
                             Purpose=room.purpose, Occupants=people)
                session.add(room)
            session.commit()

        except:
            print("Error Saving to Database")

    def load_state(self, database_name):
        """ method to load data from database into the app """
        # Load room data
        try:
            for room_name, purpose, occupants in session.query(Rooms.Name, Rooms.Purpose, Rooms.Occupants):
                individuals = occupants.split("  ")
                if purpose == "office":
                    room = Office(room_name)
                    for individual in individuals:
                        person = Person(individual)
                        room.occupants.append(person)
                    self.offices.append(room)
                    self.rooms.append(room)
                elif purpose == "living_space":
                    room = LivingSpace(room_name)
                    for individual in individuals:
                        person = Person(individual)
                        room.occupants.append(person)
                    self.living_spaces.append(room)
                    self.rooms.append(room)

        # Load People data
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
            print("Data Successfully Loaded to App")

        except:
            print("Invalid database name")
