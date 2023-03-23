#!/usr/bin/env python3
from faker import Faker

from app import app
from models import db, Production, CastMember, User


fake = Faker()

with app.app_context():

