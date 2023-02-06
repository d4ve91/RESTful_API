from unicodedata import name
from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(), unique=True)
    firstname = db.Column(db.String())
    lastname = db.Column(db.String())
    password = db.Column(db.String())
    emailadress = db.Column(db.String())
    failed_attempts = db.Column(db.Integer(), default=0)

    def __init__(self, firstname, lastname, emailadress, password, username, failed_attempts=0):
        self.firstname = firstname
        self.lastname = lastname
        self.emailadress = emailadress
        self.password = password
        self.username = username
        self.failed_attempts = failed_attempts

    def convert_to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'password': self.password,
            'emailadress': self.emailadress,
            'failed_attempts': self.failed_attempts
        }
