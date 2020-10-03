import unittest

from models.user import *


class TestUser(unittest.TestCase):

    def test_add_user(self):
        user1 = User("Trevor")
        self.assertEqual("Trevor", user1.name)
