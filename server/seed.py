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

    crime2 = Crime(
        name="Skiing Intoxicated",
        description="""
            Wyoming: No person shall move uphill on any passenger 
            tramway or use any ski slope or trail while such person's ability
            to do so is impaired by the consumption of alcohol or by the use
            of any illicit controlled substance or other drug as defined by
            W.S. 35-7-1002.
        """,
        lethal=False,
        misdemeanor=True,
        felony=False
    )

    crime3 = Crime(
        name="Lewd and lascivious cohabitation and conduct before marriage",
        description="""
            West Virginia: If any persons, not married to each other, lewdly 
            and lasciviously associate and cohabit together, or, whether 
            married or not, be guilty of open or gross lewdness and 
            lasciviousness, they shall be guilty of a misdemeanor, and, upon 
            conviction, shall be fined not less than fifty dollars, and may, 
            in the discretion of the court, be imprisoned not exceeding six 
            months, and, upon a repetition of the offense, they shall, upon 
            conviction, be confined in jail not less than six nor more than 
            twelve months.
        """,
        lethal=False,
        misdemeanor=True,
        felony=False
    )

    crime4 = Crime(
        name="Seduction under promise of marriage",
        description="""
            South Carolina: A male over the age of sixteen years who by means 
            of deception and promise of marriage seduces an unmarried woman 
            in this State is guilty of a misdemeanor and, upon conviction, 
            must be fined at the discretion of the court or imprisoned not 
            more than one year.
        """,
        lethal=False,
        misdemeanor=True,
        felony=False
    )

    crime5 = Crime(
        name="Dealing in infant children",
        description="""
            Pennsylvania: A person is guilty of a misdemeanor of the first 
            degree if he deals in humanity, by trading, bartering, buying, 
            selling, or dealing in infant children.
        """,
        lethal=False,
        misdemeanor=True,
        felony=False
    )

    crime6 = Crime(
        name="Practicing occult arts",
        description="""
            Oregon: No person shall engage in the practice of fortune telling, 
            astrology, phrenology, palmistry, clairvoyance, mesmerism or 
            spiritualism, or conduct any spiritualistic readings or 
            exhibitions of any such character for hire or profit; provided, 
            however, that this section shall not be deemed to prohibit any 
            person from conducting or carrying on any of the abovementioned 
            arts if duly licensed to do so under any of the ordinances of 
            the city.
        """,
        lethal=False,
        misdemeanor=True,
        felony=False
    )

    crime7 = Crime(
        name="Eavesdropping",
        description="""
            Oklahoma: Every person guilty of secretly loitering about any 
            building, with intent to overhear discourse therein, and to repeat 
            or publish the same to vex, annoy, or injure others, is guilty of 
            a misdemeanor.
        """,
        lethal=False,
        misdemeanor=True,
        felony=False
    )

    crimes = [crime1, crime2, crime3, crime4, crime5, crime6, crime7]

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