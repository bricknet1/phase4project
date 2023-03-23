#!/usr/bin/env python3
from faker import Faker

from app import app
from models import db


fake = Faker()

with app.app_context():

