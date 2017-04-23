""" Person model """
# Class Person


class Person(object):
    # Default constructor.
    def __init__(self, name=None, person_id=None, role=None, wants_accomodation=None):
        self.name = name
        self.id = id
        self.role = role
        self.wants_accomodation = wants_accomodation


"""Model for Fellow"""


class Fellow(Person):

    def add_person():
        # Prompt for Fellow details
        new_fellow = ((input("Enter Firstname Secondname role wants_accomodation separated by space  ")))
        return new_fellow


"""Model for Staff"""


class Staff(Person):
    def add_person(self):
        new_staff = ((input("Enter Firstname Secondname role separated by space  ")))
        return new_staff
