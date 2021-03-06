from flask import Flask, render_template, request, redirect, Blueprint

from models.fixture import Fixture
from models.team import Team


import repositories.team_repository as team_repository
import repositories.fixture_repository as fixture_repository

fixtures_blueprint = Blueprint("fixtures", __name__)

@fixtures_blueprint.route("/fixtures")
def fixtures():
    fixtures = fixture_repository.select_all()
    return render_template("/fixtures/index.html", fixtures=fixtures)

@fixtures_blueprint.route("/fixtures/new")
def new_fixture():
    team1 = team_repository.select_all()
    team2 = team_repository.select_all()
    return render_template("/fixtures/new.html", team1=team1, team2=team2)

@fixtures_blueprint.route("/fixtures", methods=['POST'])
def create_fixture():
    team1 = request.form["team1_id"]
    team2 = request.form["team2_id"]
    team1 = team_repository.select(team1)
    team2 = team_repository.select(team2)
    new_fixture = Fixture(team1, team2)
    fixture_repository.save(new_fixture)
    return redirect("/fixtures")

@fixtures_blueprint.route("/fixtures/<id>/delete", methods= ['POST'])
def delete_fixture(id):
    fixture_repository.delete(id)
    return redirect("/fixtures")

@fixtures_blueprint.route("/fixtures/<id>", methods = ['POST'])
def update_fixture(id):
    team1_id = request.form["team1_id"]
    team2_id = request.form["team2_id"]

    team1 = team_repository.select(team1_id)
    team2 = team_repository.select(team2_id)

    team1_score = request.form["team1_score"]
    team2_score = request.form["team2_score"]
    
    fixture = Fixture(team1, team2, team1_score, team2_score, id)
    fixture_repository.update(fixture)
    return redirect("/fixtures")

@fixtures_blueprint.route("/fixtures/<id>/edit", methods = ['POST'])
def edit_fixture(id):
    fixture = fixture_repository.select(id)
    teams = team_repository.select_all()
    return render_template("/fixtures/edit.html", teams = teams, fixture=fixture)



