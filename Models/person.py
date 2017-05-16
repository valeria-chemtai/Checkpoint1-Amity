from abc import ABCMeta


class Person(object):
    """ Person model """

    __metaclass__ = ABCMeta

    def __init__(self, person_name, person_id=None,
                 role=None, wants_accomodation=None):
        self.person_name = person_name
        self.id = person_id
        self.role = role
        self.wants_accomodation = wants_accomodation


class Fellow(Person):
    """Model for Fellow"""
    def __init__(self, person_name, person_id=None,
                 role="FELLOW", wants_accomodation=""):
        Person.__init__(self, person_name, person_id, wants_accomodation)
        self.person_name = person_name
        self.person_id = person_id
        self.role = "FELLOW"
        self.wants_accomodation = wants_accomodation


class Staff(Person):
    """Model for Staff"""
    def __init__(self, person_name, person_id=None,
                 role="STAFF", wants_accomodation="N"):
        Person.__init__(self, person_name, person_id, wants_accomodation)
        self.person_name = person_name
        self.person_id = person_id
        self.role = "STAFF"
        self.wants_accomodation = "N"
