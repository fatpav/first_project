from db.run_sql import run_sql


from models.team import Team

def save(team):
    sql= "INSERT INTO teams (team_name) VALUES (%s) RETURNING team_id"
    values = [team.team_name]
    # import pdb; pdb.set_trace()
    results = run_sql(sql, values)
    team.team_id = results[0]['team_id']
    return team

def select_all():
    teams = []
     
    sql =  "SELECT * FROM teams"
    results = run_sql(sql)

    for result in results:
        team = Team(result['team_name'], result['team_id'])
        teams.append(team)
    return teams

def delete_all():
    sql = "DELETE FROM teams"
    run_sql(sql)

def select(id):
    team = None
    sql = "SELECT * FROM teams WHERE team_id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        team = Team(result['team_name'], result['team_id'])
        return team

def create_team_list(self, team_list):
    self.team_list = []
    team = Team(team_name)
    team_list.append(team)
    return team_list

def delete(team_id):
    sql = "DELETE FROM teams WHERE team_id = %s"
    values = [team_id]
    run_sql(sql, values)

def update(team):
    sql = "UPDATE teams SET team_name = %s WHERE team_id = %s"
    values = [team.team_name, team.team_id]
    run_sql(sql, values)
