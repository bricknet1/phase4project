#!/usr/bin/env python3
from faker import Faker

from app import app
from models import db, Crime, User, UserCrime

fake = Faker()

profile_photos = [
    'https://www.gannett-cdn.com/media/2017/10/08/Brevard/Brevard/636430553022690213-2017-00015068.jpg?width=390&format=pjpg&auto=webp&quality=70',
    'https://www.tampabay.com/resizer//J9N3spmfSgo7WVX6Oqy3FL584lY=/fit-in/900x506/smart/filters:fill(333)/arc-anglerfish-arc2-prod-tbt.s3.amazonaws.com/public/X6UVAXGJEEI6TAOPPAY4DVT77I.jpg',
    'https://weartv.com/resources/media/b2795e90-f748-4391-bbb3-da954a2ac2e0-medium16x9_mcdowell2.PNG?1669659246097',
    'https://media-cldnry.s-nbcnews.com/image/upload/t_fit-1500w,f_auto,q_auto:best/MSNBC/Components/Slideshows/_production/_archive/Entertainment/_Celebrity-Evergreen/ss_070724_celebmugs/today-justin-bieber-mugshot-140123.jpg',
    'https://dss.fosterwebmarketing.com/upload/1055/th-mugshot.jpg',
    'https://daveandchuckthefreak.com/wp-content/uploads/sites/8/2022/10/mugshotcrazyeyes1017.jpg',
    'https://www.denverpost.com/wp-content/uploads/2016/05/20100407__winesberry1p1.jpg?w=480',
    'https://crawfordcountynow.sagacom.com/files/2022/01/IMG_9704-586x480.jpeg',
    'https://s4.reutersmedia.net/resources/r/?m=02&d=20190312&t=2&i=1365547925&w=&fh=545&fw=810&ll=&pl=&sq=&r=2019-03-12T174119Z_32695_MRPRC14438F2680_RTRMADP_0_PEOPLE-MCGREGOR',
    'https://crawfordcountynow.sagacom.com/files/2022/02/IMG_0157-640x480.jpg'
]

with app.app_context():

    Crime.query.delete()
    User.query.delete()
    UserCrime.query.delete()

    # Create some crimes
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
    users = []

    our_user = User(
        name="Boat",
        bio="I'm a boat",
        photo="https://www.galatiyachts.com/wp-content/uploads/163925496_10159410582658573_2772931438975323239_n.jpg",
        email="boat@boat.com"
    )
    our_user.password_hash = "boat"
    users.append(our_user)

    for i in range(10):
        user = User(
            name=fake.name(),
            bio=fake.paragraph(nb_sentences=3),
            photo=profile_photos[i],
            email=fake.email()
        )
        user.password_hash = 'password'
        users.append(user)

    # user1 = User(
    #     name="Boat",
    #     email="boat@show.com"
    # )
    # user1.password_hash = "password"

    # users = [user1]

    # Create some user crimes
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