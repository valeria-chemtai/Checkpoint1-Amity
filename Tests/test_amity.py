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
        self.person = Person()
        self.fellow = Fellow()
        self.staff = Staff()
        self.room = Room()
        self.office = Office()
        self.living_space = LivingSpace()

    def tearDown(self):
        del self.amity
        del self.person
        del self.fellow
        del self.staff
        del self.room
        del self.office
        del self.living_space

    def test_create_room(self):
        """Test room is succesfully created"""
        # mocking user inputs
        fake_input = mock.Mock(side_effect=["room1", "room2", "room3", " "])
        with mock.patch("builtins.input", fake_input):
            rooms = self.amity.create_room()
        # compare actual inputs to mocked values
        self.assertEqual(rooms, ["room1", "room2", "room3"])

    def test_add_person(self):
        """Test a person/people are succesfully added"""
        # mock inputs as below
        fake_input = mock.Mock(side_effect=["OLUWAFEMI SULE FELLOW Y",
                                            "DOMINIC WALTERS STAFF",
                                            "TANA LOPEZ FELLOW Y", " "])
        with mock.patch("builtins.input", fake_input):
            persons = self.amity.add_person()
        self.assertEqual(persons, ["OLUWAFEMI SULE FELLOW Y",
                                   "DOMINIC WALTERS STAFF",
                                   "TANA LOPEZ FELLOW Y"])

    def test_reallocate_person(self):
        """Test a person is rellocated succesfully"""
        # changes in length of old_room and new_room are used
        fake = [["CARO", "VAL"], ["ROSE", "ANGIE"],
                ["CARO"], ["ROSE", "ANGIE", "VAL"]]
        fake_input = mock.Mock(side_effect=fake)
        with mock.patch("builtins.input", fake_input):
            allocation_change = self.amity.reallocate_person()
        self.assertEqual(allocation_change, fake)


if __name__ == "__main__":
    unittest.main()
