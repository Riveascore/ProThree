import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AppThree.settings')

import django

django.setup()

from AppThree.models import User

# Fake population script
from faker import Faker

fakegen = Faker()

def add_user():
  firstname = fakegen.name()
  lastname = fakegen.name()
  user = User.objects.get_or_create(firstname=firstname, lastname=lastname)

  return user

def populate(N=10):
  for entry in range(N):
    user = add_user()

if __name__ == "__main__":
  print("Populating AppThree with Users")
  populate()
  print("Done Populating!")
