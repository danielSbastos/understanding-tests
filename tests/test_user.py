from unittest import TestCase
from understanding_tests.user import User


class UserTestCase(TestCase):

    def test_user_sets_email_and_username(self):
        user = User('Daniel', 'Bastos', '18')

        self.assertEqual(user.email(), 'daniel_bastos@email.com')
        self.assertEqual(user.username(), '18Daniel')

    def test_user_rigth_string_repr(self):
        user = User('Daniel', 'Bastos', '18')

        self.assertEqual('Daniel Bastos, 18', repr(user))
