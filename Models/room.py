"""Room model"""

# class Room


class Room(object):
    room_list = []

    def __init__(self, room_name=" ", room_id=None,
                 purpose=None, max_capacity=None, occupants=[]):
        self.room_name = room_name
        self.room_id = room_id
        self.purpose = purpose
        self.max_capacity = max_capacity
        self.occupants = occupants


# class office a subclass of Room


class Office(Room):
    office_list = []

    def __init__(self, room_name=" ", room_id=None,
                 purpose="office", max_capacity=6):
        self.occupants = []
        Room.__init__(self, room_name, room_id, purpose)
        self.room_name = room_name
        self.room_id = room_id
        self.purpose = "office"


# class LivingSpace a subclass of Room


class LivingSpace(Room):
    living_space_list = []

    def __init__(self, room_name=" ", room_id=None,
                 purpose="living_space", max_capacity=4):
        self.occupants = []
        Room.__init__(self, room_name, room_id, purpose)
        self.room_name = room_name
        self.room_id = room_id
        self.purpose = "living_space"
