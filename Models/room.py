"""Room model"""

# class Room


class Room(object):
    def __init__(self, name=" ", room_id=None,
                 purpose=None, occupants=[]):
        self.name = name
        self.room_id = room_id
        self.purpose =purpose
        self.occupants = occupants


# class office a subclass of Room


class Office(Room):
    def __init__(self, name=" ", room_id=None,
                 purpose=None, occupants=[], max_capacity=6):
        Room.__init__(self, name, room_id, purpose, occupants)
        self.name = name
        self.room_id = room_id
        self.purpose =purpose
        self.occupants = occupants
        self.max_capacity = 6
        

# class LivingSpace a subclass of Room


class LivingSpace(Room):
    def __init__(self, name=" ", room_id=None,
                 purpose=None, occupants=[], max_capacity=4):
        Room.__init__(self, name, room_id, purpose, occupants)
        self.name = name
        self.room_id = room_id
        self.occupants = occupants
        self.purpose = purpose
        self.max_capacity = 4

