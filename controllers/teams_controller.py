from flask import Blueprint, Flask, redirect, render_template, request, url_for

from models.team import Team
import repositories.team_repository as team_repository

team_blueprint = Blueprint("teams", __name__)

@team_blueprint.route('/teams')
def teams():
    teams = team_repository.select_all()
    return render_template("teams/new.html", users=users)
    
@team_blueprint.route('/teams/new')
def new_team():
    return render_template('/teams/new.html')

@team_blueprint.route('/teams', methods=['POST'])
def create_team():
    name = request.form["name"]
    new_team = Team(name)
    team_repository.save(new_team)
    return redirect('/teams/new.html')

@team_blueprint.route('/teams/<id>/delete', methods=['POST'])
def delete_team(id):
    team_repository.delete(id)
    return redirect('/teams')


