#!/usr/bin/env python3
from faker import Faker
import random

from app import app
from models import db, Crime, User, UserCrime, Post, Friendship, Message

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

profile_bios = [
    'Canadian singer, songwriter and actor who rose to fame as a teenager with his pop hits.',
    'American actor and producer known for his roles in popular films like "Top Gun," "Mission: Impossible" and "Jerry Maguire."',
    'Irish retired mixed martial artist and boxer who is widely considered one of the greatest fighters in the sport\'s history.',
    'British singer, songwriter and actor known for his innovative approach to music and his androgynous stage presence.',
    'American rapper, songwriter, and record producer known for his controversial lyrics and dynamic delivery.',
    'Canadian actor known for his roles in action films like "The Matrix" and "John Wick."',
    'American actor known for his roles in popular films like "Iron Man," "Sherlock Holmes" and "Chaplin."',
    'American singer, actor and cultural icon widely known as the "King of Rock and Roll."',
    'American television personality, socialite and businesswoman known for her role in the reality show "Keeping Up with the Kardashians."',
    'American rapper, singer, and actor known for his laid-back delivery and unique voice.',
    'American actress and singer known for her roles in films like "The Parent Trap," "Mean Girls" and "Freaky Friday."'
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

post_content = [
    "I love crime so much, I think I should start a fan club for it.",
    "Crime is like my daily multivitamin, I just can't function without it.",
    "If loving crime is wrong, I don't want to be right.",
    "I'm not a criminal, I'm a crime enthusiast.",
    "I like my crimes like I like my coffee - strong, daring, and a little bit risky.",
    "Breaking the law is my favorite hobby, and I'm darn good at it too.",
    "My mom always said I was destined for greatness, but I think she meant greatness in the criminal underworld.",
    "I don't always commit crimes, but when I do, I do them with style.",
    "Some people collect stamps, I collect criminal records.",
    "I'm like a modern-day Robin Hood, except I keep all the loot for myself.",
    "If crime was an Olympic sport, I'd have a gold medal in every event.",
    "I've always had a knack for breaking the rules, and crime is just the natural progression of that.",
    "I'm not sure what's more exhilarating - committing the crime or getting away with it.",
    "Crime is my favorite form of self-expression.",
    "They say crime doesn't pay, but I've got a pretty sweet criminal empire going if I do say so myself.",
    "I'm like a kid in a candy store when it comes to committing crimes.",
    "I've never met a crime I didn't like.",
    "I'm not addicted to crime, I just really, really enjoy it.",
    "Crime is my way of rebelling against society's boring rules and regulations.",
    "I love the thrill of the chase, especially when it involves the police.",
    "I'm like a superhero, except my superpower is committing crimes.",
    "If I had a dollar for every crime I've committed, I'd be a millionaire.",
    "Crime is like a puzzle that I can't resist solving.",
    "I may be a criminal, but at least I'm a happy criminal.",
]

message_content = ["Hi there!","How are you?","What are you up to?","Do you want to hang out later?","I'm sorry, I can't make it.","Congratulations on your crimes!","Happy birthday!","Thank you so much!","Can you please send me the file?","I'm running late, sorry!","Are you free for a call tomorrow?","Have a great weekend!","Did you watch the game last night?","Let's meet at the park at 2 pm.","I miss you!",]


with app.app_context():

    Crime.query.delete()
    User.query.delete()
    UserCrime.query.delete()
    Post.query.delete()
    Friendship.query.delete()
    Message.query.delete()

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
        description="Wyoming: No person shall move uphill on any passenger tramway or use any ski slope or trail while such person's ability to do so is impaired by the consumption of alcohol or by the use of any illicit controlled substance or other drug as defined by W.S. 35-7-1002.",
        lethal=False,
        misdemeanor=True,
        felony=False
    )

    crime3 = Crime(
        name="Lewd and Lascivious Cohabitation and Conduct Before Marriage",
        description="West Virginia: If any persons, not married to each other, lewdly and lasciviously associate and cohabit together, or, whether married or not, be guilty of open or gross lewdness and lasciviousness, they shall be guilty of a misdemeanor, and, upon conviction, shall be fined not less than fifty dollars, and may, in the discretion of the court, be imprisoned not exceeding six months, and, upon a repetition of the offense, they shall, upon conviction, be confined in jail not less than six nor more than twelve months.",
        lethal=False,
        misdemeanor=True,
        felony=False
    )

    crime4 = Crime(
        name="Seduction Under Promise of Marriage",
        description="South Carolina: A male over the age of sixteen years who by means of deception and promise of marriage seduces an unmarried woman in this State is guilty of a misdemeanor and, upon conviction, must be fined at the discretion of the court or imprisoned not more than one year.",
        lethal=False,
        misdemeanor=True,
        felony=False
    )

    crime5 = Crime(
        name="Dealing in Infant Children",
        description="Pennsylvania: A person is guilty of a misdemeanor of the first degree if he deals in humanity, by trading, bartering, buying, selling, or dealing in infant children.",
        lethal=False,
        misdemeanor=True,
        felony=False
    )

    crime6 = Crime(
        name="Practicing Occult Arts",
        description="Oregon: No person shall engage in the practice of fortune telling, astrology, phrenology, palmistry, clairvoyance, mesmerism or spiritualism, or conduct any spiritualistic readings or exhibitions of any such character for hire or profit; provided, however, that this section shall not be deemed to prohibit any person from conducting or carrying on any of the abovementioned arts if duly licensed to do so under any of the ordinances of the city.",
        lethal=False,
        misdemeanor=True,
        felony=False
    )

    crime7 = Crime(
        name="Eavesdropping",
        description="Oklahoma: Every person guilty of secretly loitering about any building, with intent to overhear discourse therein, and to repeat or publish the same to vex, annoy, or injure others, is guilty of a misdemeanor.",
        lethal=False,
        misdemeanor=True,
        felony=False
    )

    crime8 = Crime(
        name="Canary Whistling",
        description="California: it is against the law to whistle for a lost canary before 7 am.",
        lethal=False,
        misdemeanor=True,
        felony=False
    )

    crime9 = Crime(
        name="Giraffe Tying",
        description="Georgia: it is illegal to tie a giraffe to a telephone pole or street lamp.",
        lethal=False,
        misdemeanor=True,
        felony=False
    )

    crime10 = Crime(
        name="Bare-Handed Fish Catching",
        description="Indiana: it is illegal to catch a fish with your bare hands.",
        lethal=False,
        misdemeanor=True,
        felony=False
    )

    crime11 = Crime(
        name="Sale Blue Ducklings",
        description="Kentucky: it is illegal to dye a duckling blue and offer it for sale unless more than six are for sale at once.",
        lethal=False,
        misdemeanor=True,
        felony=False
    )

    crime12 = Crime(
        name="Feather Duster Tickling",
        description="Maine: it is unlawful to tickle women under the chin with a feather duster.",
        lethal=False,
        misdemeanor=True,
        felony=False
    )

    crime13 = Crime(
        name="Elephant Plowing",
        description="North Carolina: it is illegal to use elephants to plow cotton fields.",
        lethal=False,
        misdemeanor=True,
        felony=False
    )

    crime14 = Crime(
        name="Dollar Bill Pranking",
        description="Pennsylvania: it is illegal to tie a dollar bill to a string and pull it away when someone tries to pick it up.",
        lethal=False,
        misdemeanor=True,
        felony=False
    )

    crime15 = Crime(
        name="Comedic Mustache Wearing",
        description="Alabama: it is illegal to wear a fake mustache in church that causes laughter.",
        lethal=False,
        misdemeanor=True,
        felony=False
    )

    crimes = [crime1, crime2, crime3, crime4, crime5, crime6, crime7, crime9, crime10, crime11, crime12, crime13, crime14, crime15]

    # Create some users
    print('Creating users...')
    users = []

    our_user = User(
        name="Boat",
        bio="I'm a boat.",
        photo="https://www.galatiyachts.com/wp-content/uploads/163925496_10159410582658573_2772931438975323239_n.jpg",
        email="boat@boat.com",
        is_admin=True
    )
    our_user.password_hash = "boat"
    users.append(our_user)

    for i in range(11):
        user = User(
            name=profile_names[i],
            bio=profile_bios[i],
            photo=profile_photos[i],
            email=fake.email()
        )
        user.password_hash = 'password'
        users.append(user)

    # Create some user crimes
    print('Creating user crimes...')
    usercrimes = []
    for i in range(40):
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
            content=post_content[i],
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

    # Create some messages
    print('Creating messages...')
    messages = [
        Message(sender_id=1, receiver_id=2, content='Hey dude!'),
        Message(sender_id=2, receiver_id=1, content='Hey!'),
        Message(sender_id=2, receiver_id=1, content='Been a while!'),
        Message(sender_id=1, receiver_id=2, content='Yeah, I have been avoiding you.')
    ]
    for i in range(15):
        message = Message(
            sender_id=random.randint(3, 11),
            receiver_id=random.randint(3, 11),
            content=message_content[i]
        )
        posts.append(message)

    print('Adding to database...')
    db.session.add_all(crimes)
    db.session.add_all(users)
    db.session.add_all(usercrimes)
    db.session.add_all(posts)
    db.session.add_all(friendships)
    db.session.add_all(messages)
    db.session.commit()

    print('Donzoe')