__author__ = 'tinkpad'
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from common import util

db = util.get_db()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(320), unique=True)
    password = db.Column(db.String(32), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            # 'time': Date.unix_to_human(self.create_time),
             'email': self.email,
             'password': self.password,
        }
    def to_dict(self):
        return dict(
            id=self.id,
            username=self.username,
            email=self.email,
            password=self.password)
