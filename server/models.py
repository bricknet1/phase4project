from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from sqlalchemy.ext.hybrid import hybrid_property
from config import db, bcrypt

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    bio = db.Column(db.String)
    photo = db.Column(db.String)
    is_admin = db.Column(db.Boolean, default=False)
    email = db.Column(db.String)

    _password_hash = db.Column(db.String)

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

# class Crime(db.Model, SerializerMixin):

# class UserCrime(db.Model, SerializerMixin):

# class Messages(db.Model, SerializerMixin):
