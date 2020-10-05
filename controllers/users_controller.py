
from flask import Blueprint, Flask, redirect, render_template, request

from models.user import User
import repositories.user_repository as user_repository

user_blueprint = Blueprint("users", __name__)

@user_blueprint.route('/users/new_user', methods=['POST'])
def new_user():
    return render_template("users/new_user.html")