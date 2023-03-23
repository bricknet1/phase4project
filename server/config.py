#!/usr/bin/env python3

from flask import Flask, request, make_response, session, jsonify, abort
from flask_migrate import Migrate
from flask_restful import Api
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
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
