from flask import Flask, render_template, request, redirect
from flask import Blueprint

import repositories.user_repository as user_repository
import repositories.team_repository as team_repository

fixtures_blueprint = Blueprint("fixtures" __name__)

