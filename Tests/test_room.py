from unittest import TestCase, mock
from Models.room import Room, Office, LivingSpace

"""Unittest for class Room"""


class TestRoom(TestCase):
    def setUp(self):  # setUp so that Room() will be called as self.room
        self.room = Room()

    def tearDown(self):  # tearDown to delete self.room after every
        del self.room

