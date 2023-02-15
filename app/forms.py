from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class snowmanForm(FlaskForm):
	guess1 = StringField('Guess 1', validators=[DataRequired()])
	guess2 = StringField('Guess 2', validators=[DataRequired()])
	guess3 = StringField('Guess 3', validators=[DataRequired()])
	submit = SubmitField('Submit Guesses')