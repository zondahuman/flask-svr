__author__ = 'tinkpad'

from flask import Flask
from flask.ext.script import Manager
from flask.ext.sqlalchemy import SQLAlchemy


def get_db():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost:3306/abin?charset=utf8mb4'
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

    db = SQLAlchemy(app)
    return db


