from flask import Flask, render_template, request, redirect, Blueprint

from models.fixture import Fixture


import repositories.team_repository as team_repository
import repositories.fixture_repository as fixture_repository

fixtures_blueprint = Blueprint("fixtures", __name__)

@fixtures_blueprint.route("/fixtures")
def fixtures():
    fixtures = fixture_repository.select_all()
    return render_template("/fixtures/index.html", fixtures=fixtures)

@fixtures_blueprint.route("/fixtures/new")
def new_fixture():
    teams = team_repository.select_all()
    return render_template("/fixtures/new.html", teams=teams)

@fixtures_blueprint.route("/fixtures", methods=['POST'])
def create_fixture():
    team1_id = request.form["team1_id"]
    team2_id = request.form["team2_id"]
    team1 = team_repository.select(team1_id)
    team2 = team_repository.select(team2_id)
    new_fixture = Fixture(team1, team2)
    fixture_repository.save(new_fixture)
    return redirect("/fixtures")