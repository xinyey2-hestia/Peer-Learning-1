from application import db
from flask_login import LoginManager, UserMixin, \
    login_required, login_user, logout_user


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    notes = db.Column(db.String(128), index=True, unique=False)

    def __init__(self, notes):
        self.notes = notes

    def __repr__(self):
        return '<Data %r>' % self.notes


class User(UserMixin, db.Model):
    email = db.Column(db.String(120), primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    type = db.Column(db.String(50))

    def __init__(self, email, password, type="", name=""):
        self.email = email
        self.name = name
        self.password = password
        self.type = type

    def get_id(self):
        return self.email

    def is_authenticated(self):
        return True

    def __repr__(self):
        return '<User\tname: %s\temail: %s\tpassword: %s\ttype: %s>' % (self.name, self.email, self.password, self.type)
