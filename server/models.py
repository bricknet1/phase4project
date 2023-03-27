from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from sqlalchemy.ext.hybrid import hybrid_property
from config import db, bcrypt
from sqlalchemy.ext.associationproxy import association_proxy

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    serialize_rules = ('-_password_hash', '-user_crimes', 'crimes')

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    bio = db.Column(db.String)
    photo = db.Column(db.String)
    is_admin = db.Column(db.Boolean, default=False)
    email = db.Column(db.String)

    _password_hash = db.Column(db.String)

    user_crimes = db.relationship('UserCrime', backref='users')

    crimes = association_proxy('user_crimes', 'crimes')

    @hybrid_property
    def password_hash(self):
        return self._password_hash

    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password.encode('utf-8'))

# class Post(db.Model, SerializerMixin):

# class Friendship(db.Model, SerializerMixin):

class Crime(db.Model, SerializerMixin):
    __tablename__ = 'crimes'

    serialize_rules = ('-user_crimes',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    lethal = db.Column(db.Boolean)
    misdemeanor = db.Column(db.Boolean)
    felony = db.Column(db.Boolean)

    user_crimes = db.relationship('UserCrime', backref='crimes')

    users = association_proxy('user_crimes', 'users')

class UserCrime(db.Model, SerializerMixin):
    __tablename__ = 'user_crimes'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    crime_id = db.Column(db.Integer, db.ForeignKey('crimes.id'))
    date = db.Column(db.String)
    caught = db.Column(db.Boolean)
    convicted = db.Column(db.Boolean)

# class Messages(db.Model, SerializerMixin):
