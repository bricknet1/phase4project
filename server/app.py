#!/usr/bin/env python3

from flask import Flask, request, make_response, abort, session, jsonify
from flask_migrate import Migrate

from flask_restful import Api, Resource
from werkzeug.exceptions import NotFound, Unauthorized

from flask_cors import CORS
from flask_bcrypt import Bcrypt
from models import db

app = Flask(__name__)
CORS(app)
bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

app.secret_key = b'U\x19}J\x15O\xa7\xff\x9b\x12\x85\xa2a\x8ex\xd9'

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)






if __name__ == '__main__':
    app.run(port=5555, debug=True)