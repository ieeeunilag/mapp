# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for, \
                  abort

# Import password / encryption helper tools
from werkzeug import check_password_hash, generate_password_hash

from mapp import app
# Import the database object from the main app module
from mapp import db

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_home = Blueprint('home', __name__, url_prefix='/home')

# Set the route and accepted methods
@app.route('/', methods=['GET', 'POST'])
@mod_home.route('/index/', methods=['GET', 'POST'])
def index():

    #if not session.get('logged_in'):
        #abort(401)
    return render_template("home/index.html")
