from flask import Flask, render_template, request, redirect, blueprnt


import repositories.user_repository as user_repository
import repositories.team_repository as team_repository
import repositories.fixture_repository as fixture_repository

fixtures_blueprint = Blueprint("fixtures" __name__)



