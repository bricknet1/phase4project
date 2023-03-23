#!/usr/bin/env python3

from flask import Flask, request, make_response, session, jsonify, abort
from flask_migrate import Migrate
from flask_restful import Api, Resource
from werkzeug.exceptions import NotFound, Unauthorized
from flask_cors import CORS
from flask_bcrypt import Bcrypt

app = Flask(__name__)
CORS(app)
bcrypt = Bcrypt(app)
from models import db, User

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

app.secret_key = b'U\x19}J\x15O\xa7\xff\x9b\x12\x85\xa2a\x8ex\xd9'

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

# from config import app, db, api

class Signup(Resource):
    def post(self):
        data = request.get_json()
        user = User(email=data['email'])
        user.password_hash = data['password']
        db.session.add(user)
        db.session.commit()
        return make_response(data.to_dict(), 201)
api.add_resource(Signup, '/signup')




if __name__ == '__main__':
    app.run(port=5555, debug=True)