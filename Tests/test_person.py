from unittest import TestCase
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


if __name__ == "__main__":
    unittest.main()
