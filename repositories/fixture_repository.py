from db.run_sql import run_sql

from models.team import Team
from models.fixture import Fixture

import operator

import operator

def fixtures(team_list):
    if len(team_list) % 2:
        teams.append('Rest Day')  # if team number is odd - use 'day off' as fake team     

    rotation = list(team_list)       # copy the list

    fixtures = []
    for i in range(0, len(teams)-1):
        fixtures.append(rotation)
        rotation = [rotation[0]] + [rotation[-1]] + rotation[1:-1]

    return fixtures


teams = []

# for one match each
matches = fixtures(teams)
for f in matches:    
    print(matches)
    

