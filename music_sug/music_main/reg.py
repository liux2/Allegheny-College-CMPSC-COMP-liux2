from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from music_main.models import User

# User registrition
class RegistritionForm(FlaskForm):
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=2, max=15)]
    )
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Sign Up")

    # Validate for same username
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("That username is taken. Please choose another one.")


# User login
class LogInForm(FlaskForm):
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=2, max=15)]
    )
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")
