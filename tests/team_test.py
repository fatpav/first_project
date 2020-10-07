import unittest

from models.team import *

class TestTeam(unittest.TestCase):

    def test_team_has_name(self):
        team1 = Team("Hapsburg Saturday")
        self.assertEqual("Hapsburg Saturday", team1.name)