#!/usr/bin/env python3
from faker import Faker
import random

from app import app
from models import db, Crime, User, UserCrime, Post, Friendship

fake = Faker()

profile_names = [
    'Justin Bieber',
    'Tom Cruise',
    'Conor McGregor',
    'David Bowie',
    'Eminem',
    'Keanu Reeves',
    'Robert Downey Jr',
    'Elvis Presley',
    'Khloe Kardashian',
    'Snoop Dogg',
    'Lindsey Lohan'
]

profile_photos = [
    'https://media-cldnry.s-nbcnews.com/image/upload/t_fit-1500w,f_auto,q_auto:best/MSNBC/Components/Slideshows/_production/_archive/Entertainment/_Celebrity-Evergreen/ss_070724_celebmugs/today-justin-bieber-mugshot-140123.jpg',
    'https://imgix.ranker.com/user_node_img/50132/1002626839/original/1002626839-photo-u-2139348710?auto=format&q=60&fit=crop&fm=pjpg&dpr=2&w=375',
    'https://s4.reutersmedia.net/resources/r/?m=02&d=20190312&t=2&i=1365547925&w=&fh=545&fw=810&ll=&pl=&sq=&r=2019-03-12T174119Z_32695_MRPRC14438F2680_RTRMADP_0_PEOPLE-MCGREGOR',
    'https://i2-prod.mirror.co.uk/incoming/article7161921.ece/ALTERNATES/s1200c/David-Bowie.jpg',
    'https://toplawyer.law/wp-content/uploads/2021/07/Funny-Mugshots-Eminem-Mugshot.jpg',
    'https://toplawyer.law/wp-content/uploads/2022/01/Keanu-Reeves-Mugshot-Celebrity-Mugshots.jpg',
    'https://toplawyer.law/wp-content/uploads/2021/07/Robert-Downey-Jr-Funny-Mugshots.jpg',
    'https://images.fineartamerica.com/images/artworkimages/mediumlarge/1/elvis-presley-mug-shot-vertical-tony-rubino.jpg',
    'https://toplawyer.law/wp-content/uploads/2021/07/Khloe-Kardashian-Mugshot-Celebrity-Mugshots.jpg',
    'https://toplawyer.law/wp-content/uploads/2021/07/Rapper-Mugshots-Snoop-Dog-mugshot.jpg',
    'https://toplawyer.law/wp-content/uploads/2021/07/Lindsey-Lohan-Mugshot-Funny-Mugshots.jpg'
]

with app.app_context():

    Crime.query.delete()
    User.query.delete()
    UserCrime.query.delete()
    Post.query.delete()
    Friendship.query.delete()

    # Create some crimes
    print('Creating crimes...')
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

    # Create some users
    print('Creating users...')
    users = []

    our_user = User(
        name="Boat",
        bio="I'm a boat",
        photo="https://www.galatiyachts.com/wp-content/uploads/163925496_10159410582658573_2772931438975323239_n.jpg",
        email="boat@boat.com",
        is_admin=True
    )
    our_user.password_hash = "boat"
    users.append(our_user)

    for i in range(11):
        user = User(
            name=profile_names[i],
            bio=fake.paragraph(nb_sentences=3),
            photo=profile_photos[i],
            email=fake.email()
        )
        user.password_hash = 'password'
        users.append(user)

    # Create some user crimes
    print('Creating user crimes...')
    usercrimes = []
    for i in range(20):
        caught = random.choice([True, False])
        usercrime = UserCrime(
            user_id=random.randint(1, 11),
            crime_id=random.randint(1, 7),
            date=fake.date(),
            caught=caught,
            convicted=(False if caught == False else random.choice([True, False]))
        )
        usercrimes.append(usercrime)

    # Create some posts
    print('Creating posts...')
    posts = []
    for i in range(24):
        post = Post(
            user_id=random.randint(1, 11),
            content=fake.paragraph(nb_sentences=3),
            likes=random.randint(0, 69),
        )
        posts.append(post)

    # Create some friendships
    print('Creating friendships...')
    friendships = [
        Friendship(user_id=1, friend_id=2),
        Friendship(user_id=1, friend_id=3),
        Friendship(user_id=1, friend_id=4),
        Friendship(user_id=1, friend_id=5),
        Friendship(user_id=1, friend_id=6),
        Friendship(user_id=1, friend_id=7),
        Friendship(user_id=1, friend_id=8),
        Friendship(user_id=1, friend_id=9),
        Friendship(user_id=1, friend_id=10),
        Friendship(user_id=1, friend_id=11),

        Friendship(user_id=2, friend_id=1),
        Friendship(user_id=2, friend_id=3),
        Friendship(user_id=2, friend_id=7),
        Friendship(user_id=2, friend_id=9),
        Friendship(user_id=2, friend_id=10),

        Friendship(user_id=3, friend_id=1),
        Friendship(user_id=3, friend_id=2),
        Friendship(user_id=3, friend_id=6),
        Friendship(user_id=3, friend_id=11),

        Friendship(user_id=4, friend_id=1),
        Friendship(user_id=4, friend_id=5),
        Friendship(user_id=4, friend_id=10),

        Friendship(user_id=5, friend_id=1),
        Friendship(user_id=5, friend_id=4),
        Friendship(user_id=5, friend_id=8),
        Friendship(user_id=5, friend_id=11),

        Friendship(user_id=6, friend_id=1),
        Friendship(user_id=6, friend_id=3),
        Friendship(user_id=6, friend_id=9),

        Friendship(user_id=7, friend_id=1),
        Friendship(user_id=7, friend_id=2),
        Friendship(user_id=7, friend_id=8),
        Friendship(user_id=7, friend_id=11),

        Friendship(user_id=8, friend_id=1),
        Friendship(user_id=8, friend_id=5),
        Friendship(user_id=8, friend_id=7),

        Friendship(user_id=9, friend_id=1),
        Friendship(user_id=9, friend_id=2),
        Friendship(user_id=9, friend_id=6),
        Friendship(user_id=9, friend_id=11),

        Friendship(user_id=10, friend_id=1),
        Friendship(user_id=10, friend_id=2),
        Friendship(user_id=10, friend_id=4),

        Friendship(user_id=11, friend_id=1),
        Friendship(user_id=11, friend_id=3),
        Friendship(user_id=11, friend_id=5),
        Friendship(user_id=11, friend_id=7),
        Friendship(user_id=11, friend_id=9),
    ]

    print('Adding to database...')
    db.session.add_all(crimes)
    db.session.add_all(users)
    db.session.add_all(usercrimes)
    db.session.add_all(posts)
    db.session.add_all(friendships)
    db.session.commit()

    print('Donzoe')