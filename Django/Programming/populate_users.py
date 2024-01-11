# Python/populate_users.py
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Programming.settings")

import django
django.setup()

from Python.models import User
from faker import Faker

fake = Faker()

def populate_users(n):
    for _ in range(n):
        User.objects.create(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email()
        )

if __name__ == '__main__':
    populate_users(10)  # Change 10 to the desired number of fake users
