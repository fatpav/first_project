import unittest

from models.fixture import *
from models.team import Team


class TestFixture(unittest.TestCase):

    def __init__(self,teams):

        teams = ["Team1", "Team2", "Team3", "Team4", "Team5"]

    # def test_create_fixture(self):
    #     team1 = Team("Hapsburg Saturday", id)
    #     team2 = Team("Melchester Rovers", id)
    #     self.assertEqual(["Hapsburg Saturday", "Melchester Rovers"], Fixture.create_fixture())
