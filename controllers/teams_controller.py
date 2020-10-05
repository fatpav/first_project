from flask import Blueprint, Flask, redirect, render_template, request, url_for

from models.team import Team
import repositories.team_repository as team_repository

team_blueprint = Blueprint("teams", __name__)

@team_blueprint.route('/teams')
def teams():
    teams = team_repository.select_all()
    return render_template("teams/new.html", teams=teams)
    
@team_blueprint.route('/teams/new')
def new_team():
    return render_template('/teams/new.html')


@team_blueprint.route('/teams/index')
def new_team_list():
    return render_template('/teams/index.html')

@team_blueprint.route('/teams', methods=['POST'])
def create_team_list():

    team_list = request.form.keys()

    for key in team_list:
        team = request.form[key]
        new_team = Team(team)
        team_repository.save(new_team)
    
    # import pdb; pdb.set_trace()
    
    return redirect('/teams/index')

@team_blueprint.route('/teams/index')
def list_teams():
    teams = team_repository.select_all()
    return render_template("teams/index.html", teams=teams)





# @team_blueprint.route('/teams/<id>/delete', methods=['POST'])
# def delete_team(id):
#     team_repository.delete(id)
#     return redirect('/teams/index.html')





