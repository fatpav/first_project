import pdb

from models.fixture import Fixture

from models.team import Team

import repositories.fixture_repository as fixture_repository
import repositories.team_repository as team_repository

fixture_repository.delete_all()
team_repository.delete_all()

team1 = Team("Hibs")
team_repository.save(team1)

team2 = Team("Hearts")
team_repository.save(team2)

team3 = Team("Celtic")
team_repository.save(team3)

team4 = Team("GB")
team_repository.save(team4)

fixture1 = Fixture(team1, team2)
fixture_repository.save(fixture1)

fixture2 = Fixture(team3, team4)
fixture_repository.save(fixture2)

pdb.set_trace()