"""Room model"""

# class Room


class Room(object):
    def __init__(self, name=None, room_id=None):
        self.name = name
        self.room_id = room_id

    def create_room(self):
<<<<<<< HEAD
=======

>>>>>>> 055a3862bc55c66c93a09e58ae89cfb49d08177e
        # prompt for room names
        rooms_available = []
        while True:
            new_room = input("Room {}'s name: ". format(
                len(rooms_available) + 1))
            if not new_room:
                break
            rooms_available.append(new_room)
        return rooms_available

<<<<<<< HEAD

=======
>>>>>>> 055a3862bc55c66c93a09e58ae89cfb49d08177e
# class office a subclass of Room


class Office(Room):
    pass

# class LivingSpace a subclass of Room


class LivingSpace(Room):
    pass
