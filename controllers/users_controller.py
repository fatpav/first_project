
from flask import Blueprint, Flask, redirect, render_template, request

from models.user import User
import repositories.user_repository as user_repository

user_blueprint = Blueprint("users", __name__)

@user_blueprint.route('/users/new_user', methods=['POST'])
def new_user():
    return render_template("users/new_user.html")

@user_blueprint.route('/users/current_users', methods= ['POST'])
def users():
    users = user_repository.select_all()
    return render_template("users/current_users.html", users=users)

# @user_blueprint.route('/users/new_user', methods=['POST'])
# def create_user():
#     name = request.form["name"]
#     new_user = User(name)
#     user_repository.save(new_user)
#     return redirect('/index.html')