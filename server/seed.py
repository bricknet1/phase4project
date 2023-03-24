#!/usr/bin/env python3
from faker import Faker

from app import app
from models import db, Crime, User, UserCrime


fake = Faker()

with app.app_context():

    Crime.query.delete()
    User.query.delete()
    UserCrime.query.delete()

    crime1 = Crime(
        name="Triple Bingo",
        description="Hosting more than 2 games of bingo for seniors per week in the state of Minnesota",
        lethal=False,
        misdemeanor=True,
        felony=False
    )

    crimes = [crime1]

    user1 = User(
        name="Boat",
        email="boat@show.com"
    )
    user1.password_hash = "password"

    users = [user1]

    usercrime1 = UserCrime(
        user_id=1,
        crime_id=1,
        date="12/2/85",
        caught=False,
        convicted=False
    )

    usercrimes = [usercrime1]

    db.session.add_all(crimes)
    db.session.add_all(users)
    db.session.add_all(usercrimes)
    db.session.commit()