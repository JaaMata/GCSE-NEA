from hashlib import sha256
from random import choice
from string import ascii_lowercase
from datetime import date
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from db import UserModel, StudentModel

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///main.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class User:
    def __init__(self, username) -> None:
        self.password = None
        self.username = username

    def assign_password(self, password):
        hashed = sha256()
        hashed.update(bytes(password, "utf-8"))
        hash = hashed.hexdigest()
        self.password = hash
        print(hash)

    def save_user(self):
        user = UserModel(username=self.username, password=self.password)
        db.session.add(user)
        db.session.commit()


class Student:
    def __init__(
        self,
        forname,
        lastname,
        date_of_birth,
        home_address,
        home_phone_number,
        tutor_group,
    ) -> None:

        self.id = self.generate_id()
        self.forname = forname
        self.lastname = lastname
        self.date_of_birth = date_of_birth
        self.home_address = home_address
        self.home_phone_number = home_phone_number
        self.tutor_group = tutor_group
        self.unique_school_email = self.generate_unique_school_email()

    def generate_id(self):
        string = ""
        lst = list(ascii_lowercase)
        for i in range(13):
            string = string + str(choice(lst))
        return string

    def generate_unique_school_email(self):
        email = self.lastname.lower()[:3] + self.forname.lower()[:3]
        email += "@treeroadschool.derbyshire.sch.uk"
        return email

    def save_student(self):
        student = StudentModel(
            id=self.id,
            first_name=self.forname,
            last_name=self.lastname,
            date_of_birth=self.date_of_birth,
            home_address=self.home_address,
            home_phone_number=self.home_phone_number,
            tutor_group=self.tutor_group,
            unique_school_email=self.unique_school_email,
        )
        db.session.add(student)
        db.session.commit()


#s1 = Student(
#    "Jimi",
#    "Wilson",
#    date(2021, 9, 24),
#    "10 stanton moor view",
#   743567736,
#    "11GPR",
#)
#s1.save_student()


# u1 = User("jimi")
# u1.assign_password("Emerald15")
# u1.save_user()



class MainApp(tk.Tk)