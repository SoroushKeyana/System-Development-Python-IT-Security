# populate_data.py
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'life.settings')

import django
django.setup()

from djangoLife.models import Topic, Webpage, AccessRecord
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

def generate_fake_topic():
    return Topic.objects.get_or_create(top_name=fake.word())[0]

def generate_fake_webpage(topic):
    name = fake.company()
    url = fake.url()
    return Webpage.objects.get_or_create(topic=topic, name=name, url=url)[0]

def generate_fake_access_record(webpage):
    name = webpage
    date = fake.date_between(start_date='-30d', end_date='today')
    return AccessRecord.objects.get_or_create(name=name, date=date)[0]

def populate_data(num_entries=10):
    for _ in range(num_entries):
        topic = generate_fake_topic()
        webpage = generate_fake_webpage(topic)
        access_record = generate_fake_access_record(webpage)

if __name__ == '__main__':
    populate_data()
