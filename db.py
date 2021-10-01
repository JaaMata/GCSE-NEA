from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///main.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return "<User %r>" % self.username


class StudentModel(db.Model):
    id = db.Column(db.String(13), primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    home_address = db.Column(db.String(100), nullable=False)
    home_phone_number = db.Column(db.Integer)
    tutor_group = db.Column(db.String(5), nullable=False)
    unique_school_email = db.Column(db.String(100), unique=True, nullable=False)
