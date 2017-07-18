"""

from flask import Flask, request,redirect, url_for,  render_template
from mapp import utils
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home_page():
    params = {
    }
    return "Home"

import mapp.views.radiography
if __name__ == '__main__':
    app.debug = True
    app.run()
"""

# Import flask and template operators
from flask import Flask, render_template

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')
app.config.setdefault(
            'SQLALCHEMY_TRACK_MODIFICATIONS', True
        )
# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable (mod_auth)
from mapp.mod_home import controllers
from mapp.mod_auth.controllers import mod_auth
from mapp.mod_home.controllers import mod_home
from mapp.mod_radiography.controllers import mod_radiography


# Register blueprint(s)
app.register_blueprint(mod_auth)
app.register_blueprint(mod_home)
app.register_blueprint(mod_radiography)
# app.register_blueprint(xyz_module)
# ..

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()
