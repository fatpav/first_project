from db.run_sql import run_sql

from models.team import Team
from models.fixture import Fixture
import repositories.team_repository as team_repository


def save(fixture):
    sql = "INSERT INTO fixtures (team1.id, team2.id) VALUES (%s, %s) RETURNING id"
    values = [fixture.team1.id, fixture.team2.id]
    results = run_sql(sql, values)
    id = results[0]['id']

def select_all():
    fixtures = []
    sql = "SELECT * FROM fixtures"
    results =run_sql(sql)
    for result in results:
        team1 = team_repository.select(result["team1_id"])
        team2 = team_repository.select(result["team2_id"])
        fixture = Fixture(team1, team2, result["id"])
        fixtures.append(fixture)
    return fixtures

def select(id):
    sql = "SELECT FROM fixtures WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    team1 = team_repository.select(result["team1_id"])
    team2 = team_repository.select(result["team2_id"])
    fixture = Fixture(team1, team2, result["id"])
    return fixture

def delete_all():
    sql = "DELETE FROM fixtures"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM fixtures WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(fixture):
    sql = "UPDATE fixtures SET (team1_id, team2_id) = (%s, %s) WHERE id = %s"
    values = [fixture.team1.id, fixture.team2.id, fixture.id]
    run_sql(sql, values)
    


