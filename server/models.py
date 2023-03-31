from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from sqlalchemy.ext.hybrid import hybrid_property
from config import db, bcrypt
from sqlalchemy.ext.associationproxy import association_proxy

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    serialize_rules = ('-_password_hash', '-user_crimes', 'crime_list', '-posts', '-friendships', 'friends')

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    bio = db.Column(db.String)
    photo = db.Column(db.String)
    is_admin = db.Column(db.Boolean, default=False)
    email = db.Column(db.String)

    _password_hash = db.Column(db.String)

    user_crimes = db.relationship('UserCrime', backref='user')
    crimes = association_proxy('user_crimes', 'crime')

    @validates('email')
    def validate_email(self, key, email):
        if "@" not in email:
            raise ValueError("Must be a valid email address")
        return email

    @property
    def crime_list(self):
        returnlist = []
        for crime in set(self.crimes):
            for each in crime.user_crimes:
                if each.user_id == self.id:
                    crimedict = {
                        "id":each.id,
                        "name":crime.name,
                        "description":crime.description,
                        "lethal":crime.lethal,
                        "misdemeanor":crime.misdemeanor,
                        "felony":crime.felony,
                        "date":each.date,
                        "caught":each.caught,
                        "convicted":each.convicted
                    }
                    returnlist.append(crimedict)
        return returnlist

    posts = db.relationship('Post', backref='user')

    friendships = db.relationship('Friendship', foreign_keys='Friendship.friend_id', backref='user')

    friend_ids = association_proxy('friendships', 'user_id')

    messages = db.relationship('Message', foreign_keys='Message.sender_id', backref='sender')

    @property
    def friends(self):
        result = []
        friend_dicts = [f.to_dict() for f in self.friendships]
        for fd in friend_dicts:
            user = User.query.filter_by(id=fd['user_id']).first()
            result.append({
                "id": user.id,
                "name": user.name,
                "photo": user.photo
            })
        return result

    @hybrid_property
    def password_hash(self):
        return self._password_hash

    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password.encode('utf-8'))

class Post(db.Model, SerializerMixin):
    __tablename__ = 'posts'

    serialize_rules = ('-user.bio', '-user.crime_list', '-user.email', '-user.id', '-user.is_admin', '-user.friendships')

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String)
    likes = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class Crime(db.Model, SerializerMixin):
    __tablename__ = 'crimes'

    serialize_rules = ()

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    lethal = db.Column(db.Boolean)
    misdemeanor = db.Column(db.Boolean)
    felony = db.Column(db.Boolean)

    user_crimes = db.relationship('UserCrime', backref='crime', cascade='all, delete-orphan')

    users = association_proxy('user_crimes', 'user')

class UserCrime(db.Model, SerializerMixin):
    __tablename__ = 'user_crimes'

    serialize_rules = ('-user', '-crime')

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    crime_id = db.Column(db.Integer, db.ForeignKey('crimes.id'))
    date = db.Column(db.String)
    caught = db.Column(db.Boolean)
    convicted = db.Column(db.Boolean)

class Friendship(db.Model, SerializerMixin):
    __tablename__ = 'friendships'

    serialize_rules = ('-friend_id', '-user', '-friend')

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    friend_id = db.Column(db.Integer, db.ForeignKey('users.id'))

class Message(db.Model, SerializerMixin):
    __tablename__ = 'messages'

    serialize_rules = ('-sender',)

    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    receiver_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    content = db.Column(db.String)