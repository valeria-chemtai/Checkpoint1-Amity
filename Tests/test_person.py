from unittest import TestCase, mock
from Models import person


class PersonTest(TestCase):
    def test_add_person(self):
        fake_input = mock.Mock(side_effect=["A", "B", "C", ""])
        with mock.patch("builtins.input", fake_input):
            new_person = person.Person.add_person()
        self.assertEqual(new_person, ["A"])

if __name__ == '__main__':
	unittest.main()
