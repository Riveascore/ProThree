from django.db import models

# Create your models here.
class User(models.Model):
  firstname = models.CharField(max_length=26)
  lastname = models.CharField(max_length=26)
  email = models.EmailField(max_length=64)
