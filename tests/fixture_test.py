import unittest

from models.fixture import *
from models.team import Team


class TestFixture(unittest.TestCase):


    def test_create_fixture(self):
        team1 = Team("Hapsburg Saturday", id)
        team2 = Team("Melchester Rovers", id)
        self.assertEqual(["Hapsburg Saturday", "Melchester Rovers"], Fixture.create_fixture(team1.team_name, team2.team_name))