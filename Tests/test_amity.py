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
    self.assertEqual(self.amity.create_room("ACCRA", "OFFICE"),
                     "{} Exists in Amity.".format("ACCRA"))

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
    self.amity.add_person("ANGIE", "SULE", "STAFF", "N")
    self.assertEqual(self.amity.add_person("ANGIE", "SULE", "STAFF", "N"),
                     "{} Exists in Amity.".format("ANGIE SULE"))

  def test_valid_person_name(self):
    """Test valid person name"""
    self.assertEqual(self.amity.add_person(123, 123, "STAFF", "N"),
                     "Invalid Person Name")

  def test_reallocate_person_not_in_amity(self):
    """Test reallocate a person not in Amity yet"""
    self.amity.create_room("ACCRA", "OFFICE")
    self.assertEqual(self.amity.reallocate_person("ROSE", "WAMBUI",
                                                  "ACCRA"),
                     "Add {} to Amity first".format("ROSE WAMBUI"))

  def test_cannot_reallocate_person_to_unavailable_room(self):
    """Test person can not be reallocated to unavailable room """
    self.amity.create_room("ACCRA", "OFFICE")
    self.amity.add_person("ROSE", "WAMBUI", "STAFF", "N")
    self.assertEqual(self.amity.reallocate_person("ROSE", "WAMBUI", "CAIRO"),
                     "{} is not a room in Amity".format("CAIRO"))

  def test_successful_reallocation(self):
    """Test if person is successfully reallocated"""
    self.amity.create_room("Accra", "OFFICE")
    self.amity.add_person("Rose", "Wambui", "STAFF", "N")
    self.amity.create_room("Cairo", "OFFICE")
    self.assertEqual(self.amity.reallocate_person(
        "ROSE", "WAMBUI", "CAIRO"), "Reallocated Successfully")

  def test_reallocates_to_appropriate_room_type(self):
    """Test person reallocated to room type as current room"""
    self.amity.create_room("Accra", "OFFICE")
    self.amity.add_person("Rose", "Wambui", "STAFF", "N")
    self.amity.create_room("Unono", "LIVINGSPACE")
    self.assertEqual(self.amity.reallocate_person(
        "ROSE", "WAMBUI", "UNONO"), "Choose Appropriate Room Type")

  def test_print_existing_room(self):
    """Test for printing existing room"""
    self.amity.create_room("Accra", "OFFICE")
    self.assertEqual(self.amity.print_room("Accra"), "Print room successful")

  def test_print_nonexisting_room(self):
    """Test for printing nonexisting room """
    self.assertEqual(self.amity.print_room("Accra"), "Room does not exist")

  def test_print_allocations_to_file(self):
    """Test that Allocations can be printed to specified file name"""
    self.amity.create_room("Accra", "OFFICE")
    self.amity.add_person("Rose", "Wambui", "STAFF", "N")
    self.assertEqual(self.amity.print_allocations(
        "data.txt"), "Allocations Printed to data.txt")

  def test_print_allocations_not_done_if_no_rooms(self):
    """Test that allocations not printed if no rooms available in Amity"""
    self.assertEqual(self.amity.print_allocations("data.txt"), "No Rooms")

  def test_unallocated_staff_and_fellow_allocated_available_office(self):
    """Test staff and fellow who wants only office in unallocated list allocated office"""
    self.amity.add_person("ROSE", "WAMBUI", "STAFF", "N")
    self.amity.add_person("Valeria", "Chemtai", "fellow", "N")
    self.amity.create_room("Accra", "OFFICE")
    self.amity.create_room("Unono", "livingspace")
    self.assertEqual(self.amity.allocate_unallocated(
        "Rose", "Wambui"), "Member Now Allocated Office")
    self.assertEqual(self.amity.allocate_unallocated(
        "Valeria", "Chemtai"), "Member Now Allocated Office")

  def test_unallocated_fellow_allocated_office_and_living_space(self):
    """Test to show unallocated fellow who wants both office and livingspace in allocated"""
    self.amity.add_person("Valeria", "Chemtai", "fellow", "Y")
    self.amity.create_room("Accra", "office")
    self.amity.create_room("Unono", "livingspace")
    self.assertEqual(self.amity.allocate_unallocated(
        "Valeria", "Chemtai"), "Member Now Allocated Office")
    self.assertEqual(self.amity.allocate_unallocated(
        "Valeria", "Chemtai"), "Fellow Now Allocated LivingSpace")


if __name__ == "__main__":
  unittest.main()
