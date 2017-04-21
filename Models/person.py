""" Person model """
# Class Person


class Person(object):
    # Default constructor.
    def __init__(self, name, person_id, role, wants_accomodation):
        self.name = name
        self.id = id
        self.role = role
        self.wants_accomodation = wants_accomodation


"""Model for Fellow"""


class Fellow(Person):
    pass

"""Model for Staff"""


class Staff(Person):
    pass
