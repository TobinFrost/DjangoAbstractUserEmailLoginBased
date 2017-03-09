from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class MyUser(AbstractUser):
    is_sick = models.BooleanField()



class Etudiant(models.Model):
    user = models.OneToOneField(MyUser,on_delete=models.CASCADE)
    departement = models.CharField(max_length=50,name="departement")