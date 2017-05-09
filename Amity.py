"""Class Amity is the controller of the app using
the Models Views Controller concept i.e. MVC"""
import os
import random


from Models.person import Person, Fellow, Staff
from Models.room import Room, Office, LivingSpace


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
                    self.allocate_living_space(person_name, wants_accomodation)
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

    def allocate_living_space(self, person, wants_accomodation):
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
                format(person.person_name))

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

        else:
            old_room = [room for room in self.room_list if person[
                0] in room.occupants]
            room[0].occupants.append(person[0])
            old_room[0].occupants.remove(person[0])
            person[0].old_room = room[0].room_name
            print("{} was moved from {} to {}".format(
                person[0].person_name, old_room[0].room_name, room[0].room_name))
            return "Reallocated Successfully"

    """ method to add people to rooms from a text file """

    def load_people(self):
        pass

    """ method to print a list of allocations on screen
     with option to store in a txt file """

    def print_allocation(self):
        pass

    """ method to print a list of unallocated people in screen
     with option to store in a text file """

    def print_unallocated(self):
        pass

    """ method to print room name and all people allocated to that room """

    def print_room(self):
        pass

    """ method to save all data in the app into SQLite database """

    def save_state(self):
        pass

    """ method to load data from database into the app """

    def load_state(self):
        pass
