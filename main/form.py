from flask_wtf import FlaskForm
from main.model import User 
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired,Length, Email, EqualTo, ValidationError

class login_form(FlaskForm):
    username = StringField(label="Username", validators=[DataRequired(), Length(min=2,max=30)])
    email = StringField(label="Email", validators=[DataRequired(), Email()])
    password = PasswordField(label ="Password", validators= [DataRequired() ])
    submit = SubmitField(label = "Sign-in")

class Registeration(FlaskForm):
    username = StringField(label="Username", validators=[DataRequired(), Length(min=2,max=30)])
    email = StringField(label="Email", validators=[DataRequired(), Email()])
    password = PasswordField(label ="Password", validators= [DataRequired() ])
    confirm_password = PasswordField(label ="RePassword", validators= [DataRequired(), EqualTo("password")])
    submit = SubmitField(label = "Sign-up")

    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()
        if user:
            raise ValidationError("This username is been taken please chose a different one")
    

    def validate_email(self, email):
        user_email = User.query.filter_by(email = email.data).first()
        if user_email:
            raise ValidationError("Sorry this email has been taken please chose a diffent one")


    
