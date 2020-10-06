
from flask import Blueprint, Flask, redirect, render_template, request, url_for

from models.user import User
import repositories.user_repository as user_repository

user_blueprint = Blueprint("users", __name__)


@user_blueprint.route('/users')
def users():
    users = user_repository.select_all()
    return render_template("users/index.html", users=users)
    
@user_blueprint.route('/users/new')
def new_user():
    return render_template('/users/new.html')

@user_blueprint.route('/users', methods=['POST'])
def create_user():
    name = request.form["name"]
    new_user = User(name)
    user_repository.save(new_user)
    return redirect('/users')

@user_blueprint.route('/users/<id>', methods=['POST'])
def update_user(id):
    name = request.form["name"]
    user = User(name, id)
    user_repository.update(user)
    return redirect('/users')

@user_blueprint.route('/users/<id>/delete', methods=['POST'])
def delete_user(id):
    user_repository.delete(id)
    return redirect('/users')

@user_blueprint.route("/users/<id>/edit", methods=['POST'])
def edit_user(id):
    user = user_repository.select(id)
    return render_template('users/edit.html', user=user)


