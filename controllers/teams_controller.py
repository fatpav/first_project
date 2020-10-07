from flask import Blueprint, Flask, redirect, render_template, request, url_for

from models.team import Team
import repositories.team_repository as team_repository

team_blueprint = Blueprint("teams", __name__)


@team_blueprint.route('/teams/new')
def new_team():
    return render_template('/teams/new.html')

@team_blueprint.route('/teams', methods=['POST'])
def create_team():
    name = request.form["name"]
    new_team = Team(name)
    team_repository.save(new_team)
    return redirect("/teams")

@team_blueprint.route('/teams')
def teams():
    teams = team_repository.select_all()
    return render_template("teams/index.html", teams=teams)
    
@team_blueprint.route('/teams/<id>/delete', methods=['POST'])
def delete_team(id):
    team_repository.delete(id)
    return redirect('/teams')

@team_blueprint.route('/teams/<id>', methods=['POST'])
def update_team(id):
    name = request.form["name"]
    team = Team(name, id)
    team_repository.update(team)
    return redirect('/teams')

@team_blueprint.route("/teams/<id>/edit", methods=['POST'])
def edit_team(id):
    team = team_repository.select(id)
    return render_template('teams/edit.html', team=team)

@team_blueprint.route("/teams/<id>")
def show_fixtures(id):
    team = team_repository.select(id)
    fixtures = fixture_repository.show_team_fixtures(id)
    return render_template('teams/show.html', team=team, fixtures=fixtures)

