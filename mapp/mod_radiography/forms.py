# Import Form and RecaptchaField (optional)
from flask_wtf import FlaskForm # , RecaptchaField

# Import Form elements such as TextField and BooleanField (optional)
from wtforms import TextField, PasswordField,IntegerField # BooleanField

# Import Form validators
from wtforms.validators import Required, Email, EqualTo,NumberRange


# Define the login form (WTForms)

class RadiographyForm(FlaskForm):
    sur_name = TextField('Surname', [Required(message='Forgot your Surname?')])
    other_name = TextField('Other Name', [Required(message='Forgot your Other Names?')])
    address = TextField('Address', [Required(message='Forgot your Address?')])
    age = IntegerField('Age', [Required(message='Forgot your Age?'),NumberRange( min=0,message='Your Age must be greater than 0?')])
