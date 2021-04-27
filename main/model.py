from main import app, login_manager
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
db =SQLAlchemy(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    username= db.Column(db.String(20), nullable= False, unique= True)
    email = db.Column(db.String(120), nullable = True, unique= True)
    password = db.Column(db.String(60), nullable=True)

    def __repr__(self):
        return f'user({self.username})'

    