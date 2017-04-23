from unittest import TestCase, mock
from Models.room import Room, Office, LivingSpace

"""Unittest for class Room"""


class TestRoom(TestCase):
    def setUp(self):  # setUp so that Room() will be called as self.room
        self.room = Room()

    def tearDown(self):  # tearDown to delete self.room after every call
        del self.room

    def test_create_room(self):  # Test method to create new rooms
        # Mocking user inputs
        fake_input = mock.Mock(side_effect=["room1", "room2", "room3", ""])
        with mock.patch("builtins.input", fake_input):
            new_room = Room.create_room(self)
        self.assertEqual(new_room, ["room1", "room2", "room3"])


if __name__ == "__main__":
    unittest.main()
