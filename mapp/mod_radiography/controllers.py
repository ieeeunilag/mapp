# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for

# Import password / encryption helper tools
from werkzeug import check_password_hash, generate_password_hash

# Import the database object from the main app module
from mapp import db

# Import module forms
from mapp.mod_radiography.forms import RadiographyForm

# Import module models (i.e. User)
from mapp.mod_radiography.models import Radiography

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_radiography = Blueprint('radiography', __name__, url_prefix='/radiography')



# Set the route and accepted methods
@mod_radiography.route('/create', methods=['GET','POST'])
def radiography_create():


    form = RadiographyForm(request.form)

    # Verify the sign in form
    if form.validate_on_submit():
        params = {
            'sur_name': form.sur_name.data,
            'other_name': form.other_name.data,
            'address': form.address.data,
            'age': form.age.data

        }
        new_radiography = Radiography(**params)
        db.session.add(new_radiography)
        db.session.commit()
        flash('Data Added Successfully.','info')
        return redirect(url_for('radiography.radiography'))

    return render_template('radiography/radiography_single.html',form=form)

# Set the route and accepted methods
@mod_radiography.route('/')
def radiography():
    params = {
        'radiography_list': Radiography.query.all()
    }

    return render_template('radiography/radiography.html', **params)


# Set the route and accepted methods
@mod_radiography.route('/<int:id>', methods=['GET','POST'])
def radiography_single(id):


    form = RadiographyForm(request.form)

    # Verify the sign in form
    if form.validate_on_submit():
        params = {
            'sur_name': request.form['sur_name'],
            'other_name': request.form['other_name'],
            'address': request.form['address'],
            'age': request.form['age']

        }

        radiography = Radiography.query.filter_by(id=id).one()
        if radiography != []:
            radiography.sur_name = params['sur_name']
            radiography.other_name = params['other_name']
            radiography.address = params['address']
            radiography.age = params['age']
            db.session.add(radiography)
            db.session.commit()
        flash('Data Updated Successfully.','info')
        return redirect(url_for('radiography.radiography'))
    else:
        result = Radiography.query.filter_by(id=id).one()
        params = {
            'sur_name': result.sur_name,
            'other_name': result.other_name,
            'address': result.address,
            'age': result.age

        }

        form = RadiographyForm(data=params)
        return render_template('radiography/radiography_single.html',form=form)


# Set the route and accepted methods
@mod_radiography.route('/delete', methods=['POST'])
def radiography_delete():
    id = request.form['id']
    radiography = Radiography.query.filter_by(id=id).one()
    if radiography:
        db.session.delete(radiography)
        db.session.commit()
    flash('Data Deleted Successfully.','info')
    return redirect(url_for('radiography.radiography'))
