from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, Email



class RegistrationForm(FlaskForm):
    username = StringField('Usrname', validators=[DataRequired()])
    last_name = StringField('Lastname', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    email = EmailField('Email', validators=[DataRequired(),Email()])



