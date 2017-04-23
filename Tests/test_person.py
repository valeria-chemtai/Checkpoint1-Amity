from unittest import TestCase, mock
from Models.person import Person, Fellow, Staff


class FellowTest(TestCase):
    def setUp(self):
        # call Fellow(Person) as self.fellow before running tests in this class
        self.fellow = Fellow()

    def tearDown(self):
        del self.fellow  # after every test delete self.fellow

    # check that class Fellow is an instance/subclass of class Person
    def test_fellow_is_instance_of_person(self):
        self.assertTrue(self.fellow, Person)

    def test_add_person(self):
        # Test user can input Fellow details
        # mocked one object because am calling this function once here.
        fake_input = mock.Mock(side_effect=["OLU JACOBS FELLOW Y", ""])
        with mock.patch("builtins.input", fake_input):
            new_fellow = Fellow.add_person()
        self.assertEqual(new_fellow, "OLU JACOBS FELLOW Y")


class StaffTest(TestCase):
    def setUp(self):
        # call class Staff as self.staff
        self.staff = Staff()

    def teardown(self):
        del self.staff

    def test_staff_is_instance_of_person(self):
        # check if class staff is a subclass of Person
        self.assertTrue(self.staff, Person)

    def test_add_person(self):
        # Test user can input staff details i.e name and role
        # mocking inputs
        fake_input = mock.Mock(side_effect=["DOMINIC WALTERS STAFF", ""])
        with mock.patch("builtins.input", fake_input):
            new_staff = Staff.add_person(self)
        self.assertEqual(new_staff, "DOMINIC WALTERS STAFF")


if __name__ == "__main__":
    unittest.main()
