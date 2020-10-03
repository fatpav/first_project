rom db.run_sql import run_sql

from models.user import User
from models.team import Team

def save(team):
    sql= "INSERT INTO teams (name) VALUES (%s) RETURNING id"
    values = [team.name]
    results = run_sql(sql, values)
    team.team_id = results[0]['id']
    return team

def select_all():
    teams = []
     
     sql "SELECT * FROM teams"
     results = run_sql(sql)

     for row in results:
         team = Team(row['team_name'], row['id'])
         teams.append(team)
         return teams

def delete_all():
    sql = "DELETE FROM teams"
    run_sql(sql)

def select(id):
    team = None
    sql = "SELECT * FROM teams WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        team = Team(result['team_name'], result['id'])
        return team