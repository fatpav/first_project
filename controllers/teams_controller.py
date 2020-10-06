from flask import Blueprint, Flask, redirect, render_template, request, url_for

from models.team import Team
import repositories.team_repository as team_repository

team_blueprint = Blueprint("teams", __name__)


@team_blueprint.route('/teams/new')
def new_team():
    return render_template('/teams/new.html')

@team_blueprint.route('/teams/new', methods=['POST'])
def create_team_list():

    team_list = request.form.keys()

    for key in team_list: 
        team = request.form[key]
        new_team = Team(team)
        team_repository.save(new_team)
               
        
    
    # import pdb; pdb.set_trace()
    
    return redirect('/teams')

@team_blueprint.route('/teams')
def teams():
    teams = team_repository.select_all()
    return render_template("teams/index.html", teams=teams)
    
@team_blueprint.route('/teams/<team_id>/delete', methods=['POST'])
def delete_team(team_id):
    team_repository.delete(team_id)
    return redirect('/teams')

@team_blueprint.route('/teams/<team_id>', methods=['POST'])
def update_team(team_id):
    name = request.form["name"]
    team = Team(name, team_id)
    team_repository.update(team)
    return redirect('/teams')

@team_blueprint.route("/teams/<team_id>/edit", methods=['POST'])
def edit_team(team_id):
    team = team_repository.select(team_id)
    return render_template('teams/edit.html', team=team)



