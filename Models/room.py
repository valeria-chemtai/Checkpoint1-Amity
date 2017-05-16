"""Room model"""
from abc import ABCMeta


class Room(object):
    __metaclass__ = ABCMeta

    def __init__(self, room_name=" ", room_id=None,
                 purpose=None, max_capacity=None, occupants=[]):
        self.room_name = room_name
        self.room_id = room_id
        self.purpose = purpose
        self.max_capacity = max_capacity
        self.occupants = []


class Office(Room):
    def __init__(self, room_name=" ", room_id=None,
                 purpose="office", occupants=[], max_capacity=6):
        Room.__init__(self, room_name, room_id, purpose,
                      occupants, max_capacity)
        self.room_name = room_name
        self.room_id = room_id
        self.purpose = "office"
        self.occupants = []
        self.max_capacity = 6


class LivingSpace(Room):
    def __init__(self, room_name=" ", room_id=None,
                 purpose="living_space", occupants=[], max_capacity=4):
        Room.__init__(self, room_name, room_id, purpose,
                      occupants, max_capacity)
        self.room_name = room_name
        self.room_id = room_id
        self.purpose = "living_space"
        self.occupants = []
        self.max_capacity = 4
