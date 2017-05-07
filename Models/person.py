
""" Person model """
# Class Person


class Person(object):
    # Default constructor.
    total = []

    def __init__(self, person_name, person_id=None,
                 role=None, wants_accomodation=None):
        self.person_name = person_name
        self.id = person_id
        self.role = role
        self.wants_accomodation = wants_accomodation


"""Model for Fellow"""


class Fellow(Person):
    def __init__(self, person_name, person_id=None,
                 role="FELLOW", wants_accomodation="Y"):
        Person.__init__(self, person_name, person_id, wants_accomodation)
        self.person_name = person_name
        self.person_id = person_id
        self.role = "FELLOW"
        self.wants_accomodation = "Y"


"""Model for Staff"""


class Staff(Person):
    def __init__(self, person_name, person_id=None,
                 role="STAFF", wants_accomodation="N"):
        Person.__init__(self, person_name, person_id, wants_accomodation)
        self.person_name = person_name
        self.person_id = person_id
        self.role = "STAFF"
        self.wants_accomodation = "N"