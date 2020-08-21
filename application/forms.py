from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, DateField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from application.models import User, Mood

class LoginForm(FlaskForm):
    email   = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6,max=15)])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Login")

class RegisterForm(FlaskForm):
    email   = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(),Length(min=6,max=15)])
    password_confirm = PasswordField("Confirm Password", validators=[DataRequired(),Length(min=6,max=15), EqualTo('password')])
    first_name = StringField("First Name", validators=[DataRequired(),Length(min=2,max=55)])
    last_name = StringField("Last Name", validators=[DataRequired(),Length(min=2,max=55)])
    submit = SubmitField("Register Now")

    def validate_email(self,email):
        user = User.objects(email=email.data).first()
        if user:
            raise ValidationError("Email is already in use. Pick another one.")

class Mood_Form(FlaskForm):
    
    mood = StringField("Mood", validators=[DataRequired(),Length(min=3,max=55)])
    # remember_me = BooleanField("Remember Me")
    submit = SubmitField("submit")

class Todo_Form(FlaskForm):
    
    task = StringField("task", validators=[DataRequired(),Length(min=3,max=55)])
    date = DateField("date", validators=[DataRequired(),Length(min=3,max=55)])
    time= IntegerField("time", validators=[DataRequired(),Length(min=3,max=55)])
    am = StringField("task", validators=[DataRequired(),Length(min=3,max=55)])
    # remember_me = BooleanField("Remember Me")
    submit = SubmitField("td")
