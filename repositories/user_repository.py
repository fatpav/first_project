from db.run_sql import run_sql

from models.user import User
from models.team import Team

def save(user):
    sql = "INSERT INTO users (name) VALUES (%s) RETURNING id"
    values = [user.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    user.id = id

def select_all():
    users = []

    sql = "SELECT * FROM users"
    results = run_sql(sql)
    for result in results:
        user = User(result['name'], result['id'])
        users.append(user)
    return users

def select(id):
    user = None
    sql= "SELECT * FROM users WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        user = User(result['name'], result['id'])
        return user

def delete_all():
    sql = "DELETE FROM users"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM users WHERE id = %s"
    values = [id]
    run_sql(sql, values)
