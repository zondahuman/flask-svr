__author__ = 'tinkpad'


from flask import Flask
from flask import render_template
from flask import request
from flask import flash
from flask import redirect
from flask import url_for
from flask import make_response
from flask import session
from model import models
import json
from flask import jsonify
from common import serialization,ApiResponse

app = Flask(__name__)



# http://localhost:5000/find/1
@app.route('/find/<int:id>', methods=['GET'])
def find(id):
    if id:
        # user = models.User.query.filter(models.User.id == int(id)).all()
        user = models.User.query.filter_by(id=id).first()
        print "user=",user
    return serialization.jsonify_with_data(ApiResponse.APIError.OK,user=user.to_dict())


@app.route('/')
def index():
    if id:
        # user = models.User.query.filter(models.User.id == int(id)).all()
        user = models.User.query.filter_by(id=id).first()
        print "user=",user
    return serialization.jsonify_with_data(ApiResponse.APIError.OK,user=user.to_dict())

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')