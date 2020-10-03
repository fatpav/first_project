import pdb

from models.fixture import Fixture
from models.user import User
from models.team import Team

import repositories.fixture_repository as fixture_repository
import repositories.team_repository as team_repository
import repositories.fixture_repository as fixture_repository

user_repository.delete_all()

user1 = User("Paul Donegan")
user_repository.save(user1)