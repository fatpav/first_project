from flask import Flask, render_template, redirect, request, Blueprint
from templates import *
from templates.fixtures import *
from controllers.users_controller import user_blueprint


app = Flask(__name__)

app.register_blueprint(user_blueprint)

@app.route('/')
def home():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)