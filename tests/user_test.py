import unittest

from models.user import *


class TestUser(unittest.TestCase):

    def test_user_has_name(self):
        user1 = User("Trevor")
        self.assertEqual("Trevor", user1.name)
