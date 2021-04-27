from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_manager

app = Flask(__name__)

app.config["SECRET_KEY"] ='172f7c7a3564f15ff5716dec'
app.config["SQLALCHEMY_DATABASE_URI"]= 'sqlite:///db.sit'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] =False

db =SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category ='info'


from main import route