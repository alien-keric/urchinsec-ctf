from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Users(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), unique=True)
    password = db.Column(db.String())

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f"{self.username}:{self.password}"
    

class SesameKey(db.Model):
    __tablename__ = "sesame_keys"

    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String())

    def __init__(self, key):
        self.key = key

    def __repr__(self):
        return f"{self.key}"