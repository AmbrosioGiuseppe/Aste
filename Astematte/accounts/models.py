from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields.related import ForeignKey

# Create your models here.
class MyUser(AbstractUser):
    email               = models.EmailField(null=True,blank=True)
    coin                = models.IntegerField(default=3)
