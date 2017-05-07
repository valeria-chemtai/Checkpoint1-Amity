from unittest import TestCase, mock
import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from Amity import Amity
from Models.person import Person, Fellow, Staff
from Models.room import Room, Office, LivingSpace


class TestAmity(TestCase):
    def setUp(self):
        # call this function as specified for each test
        self.amity = Amity()

    def tearDown(self):
        del self.amity

    def test_create_room(self):
        """Test room is succesfully created"""

        self.assertEqual(self.amity.create_room("Accra", "OFFICE"),
                         "Room Created")
        self.assertEqual(self.amity.create_room("Unono", "LIVINGSPACE"),
                         "Room Created")

    def test_room_only_created_once(self):
        """Test room is only created once"""
        self.amity.create_room("Accra", "OFFICE")
        self.assertEqual(self.amity.create_room("Accra", "OFFICE"),
                         "{} Exists in Amity.".format("Accra"))

    def test_valid_room_names(self):
        """Test valid room name"""
        self.assertEqual(self.amity.create_room(
            123, "OFFICE"), "Invalid Room Name")

    def test_add_person(self):
        """Test a person/people are succesfully added"""
        self.amity.create_room("Accra", "OFFICE")
        self.amity.create_room("Unono", "LIVINGSPACE")
        self.assertEqual(self.amity.add_person("Dominic", "Walters", "STAFF",
                                               "N"), "Staff Added")
        self.assertEqual(self.amity.add_person("Oluwafemi", "Sule", "FELLOW",
                                               "N"), "Fellow Added")
        self.assertEqual(self.amity.add_person("Simon", "Patterson", "FELLOW",
                                               "Y"),
                         "Fellow Added and LIvingSpace Allocated")

    def test_add_existing_person(self):
        """Test person is added once"""
        self.amity.add_person("Angie", "Sule", "STAFF", "N")
        self.assertEqual(self.amity.add_person("Angie", "Sule", "STAFF", "N"),
                         "{} Exists in Amity.".format("Angie Sule"))

    def test_valid_person_name(self):
        """Test valid person name"""
        self.assertEqual(self.amity.add_person(123, 123, "STAFF", "N"),
                         "Invalid Person Name")

    def test_reallocate_person_not_in_amity(self):
        """Test reallocate a person not in Amity yet"""
        self.amity.create_room("Accra", "OFFICE")
        self.assertEqual(self.amity.reallocate_person("Rose", "Wambui",
                                                      "Accra"),
                         "Add {} to Amity first".format("Rose Wambui"))

    def test_cannot_reallocate_person_to_unavailable_room(self):
        """Test person can not be reallocated to unavailable room """
        self.amity.create_room("Accra", "OFFICE")
        self.amity.add_person("Rose", "Wambui", "STAFF", "N")
        self.assertEqual(self.amity.reallocate_person("Rose", "Wambui", "Cairo"), "{} is not a room in Amity".format("Cairo"))


if __name__ == "__main__":
    unittest.main()
