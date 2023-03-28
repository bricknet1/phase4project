#!/usr/bin/env python3

from flask import request, make_response, session, jsonify, abort
from flask_restful import Resource
from werkzeug.exceptions import NotFound, Unauthorized
from models import User, Post, Crime

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
        if user:
            if user.authenticate(data['password']):
                session['user_id'] = user.id
                return make_response(user.to_dict(), 200)
            else:
                abort(404, 'Login incorrect.')
        else:
            abort(404, 'Login incorrect.')
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

class GetUserByID(Resource):
    def get(self, id):
        try:
            id = str(id)
            user = User.query.filter_by(id=id).first()
            return make_response(user.to_dict(rules=('posts',)), 200)
        except:
            abort(404, "User not found")

    def patch(self, id):
        user = User.query.filter_by(id=id).first()
        data = request.get_json()
        if not user:
            raise NotFound
        for attr in data:
            setattr(user, attr, data[attr])
        db.session.add(user)
        db.session.commit()
        response = make_response(user.to_dict(), 200)
        return response
api.add_resource(GetUserByID, '/users/<int:id>')

class Posts(Resource):
    def get(self):
        try:
            posts = [post.to_dict() for post in Post.query.all()]
            return make_response(posts, 200)
        except Exception as e:            
            abort(404, [e.__str__()])

    def post(self):
        data = request.get_json()
        post = Post(
            user_id=session['user_id'],
            content=data['content'],
            likes=data['likes']
        )
        db.session.add(post)
        db.session.commit()
        response = make_response(post.to_dict(), 200)
        return response
api.add_resource(Posts, '/posts')

class Crimes(Resource):
    def get(self):
        try:
            crimes = [crime.to_dict(rules=('-user_crimes',)) for crime in Crime.query.all()]
            return make_response(crimes, 200)
        except Exception as e:            
            abort(404, [e.__str__()])
    def post(self):
        data = request.get_json()
        crime = Crime(
            name=data['name'],
            description=data['description']
        )
        db.session.add(crime)
        db.session.commit()
        response = make_response(crime.to_dict(), 200)
        return response
api.add_resource(Crimes, '/crimes')

class CrimeByID(Resource):
    def get(self, id):
        try:
            crime = Crime.query.filter_by(id=id).first()
            return make_response(crime.to_dict(rules=('-user_crimes',)), 200)
        except:
            abort(404, "Crime not found")
    def patch(self, id):
        crime = Crime.query.filter_by(id=id).first()
        data = request.get_json()
        if not crime:
            raise NotFound
        for attr in data:
            setattr(crime, attr, data[attr])
        db.session.add(crime)
        db.session.commit()
        response = make_response(crime.to_dict(), 200)
        return response
    def delete(self, id):
        crime = Crime.query.filter_by(id=id).first()
        if not crime:
            raise NotFound
        db.session.delete(crime)
        db.session.commit()
        return make_response('', 204)
api.add_resource(CrimeByID, '/crimes/<int:id>')

if __name__ == '__main__':
    app.run(port=5555, debug=True)