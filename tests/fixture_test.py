import unittest

from models.fixture import *
from models.team import *

class TestFixture(unittest.TestCase):


    def test_create_fixture(self):
        team1 = Team("Hapsburg Saturday")
        team2 = Team("Melchester Rovers")
        self.assertEqual("Hapsburg Saturday" "vs" "Melchester Rovers", fixture.create_fixture(team1, team2) )