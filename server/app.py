#!/usr/bin/env python3

from flask import request, make_response, session, jsonify, abort
from flask_restful import Resource
from werkzeug.exceptions import NotFound, Unauthorized
from models import User

from config import app, db, api

class Signup(Resource):
    def post(self):
        data = request.get_json()
        user = User(email=data['email'])
        user.password_hash = data['password']
        db.session.add(user)
        db.session.commit()
        return make_response(user.to_dict(), 201)
api.add_resource(Signup, '/signup')

class Login(Resource):
    def post(self):
        data = request.get_json()
        user = User.query.filter_by(email=data['email']).first()
        if user.authenticate(data['password']):
            session['user_id'] = user.id
            return make_response(user.to_dict(), 200)
api.add_resource(Login, '/login')

class AuthorizedSession(Resource):
    def get(self):
        try:
            user = User.query.filter_by(id=session['user_id']).first()
            return make_response(user.to_dict(), 200)
        except:
            abort(401, "Unauthorized")
api.add_resource(AuthorizedSession, '/authorized')

class Logout(Resource):
    def delete(self):
        session['user_id'] = None
        return make_response('', 204)
api.add_resource(Logout, '/logout')

if __name__ == '__main__':
    app.run(port=5555, debug=True)