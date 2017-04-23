"""Room model"""

# class Room


class Room(object):
    def __init__(self, name=None, room_id=None):
        self.name = name
        self.room_id = room_id

    def create_room(self):

      

# class office a subclass of Room


class Office(Room):
    pass

# class LivingSpace a subclass of Room


class LivingSpace(Room):
    pass
