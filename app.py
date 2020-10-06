from flask import Flask, render_template, redirect, request, Blueprint
from templates import *
from templates.fixtures import *
from templates.teams import *

from controllers.teams_controller import team_blueprint
from controllers.fixtures_controller import fixtures_blueprint

app = Flask(__name__)

app.register_blueprint(team_blueprint)
app.register_blueprint(fixtures_blueprint)

@app.route('/')
def home():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)