from django.db import models
from django.contrib.auth.models import User,AbstractBaseUser,UserManager


# Create your models here.
class User(AbstractBaseUser):
    username = models.CharField(max_length=100,unique=True)
    email = models.CharField(max_length=90)
    bio = models.TextField(max_length=100,blank=True)
    password = models.CharField(max_length=150)
    profile_pic = models.ImageField(upload_to='images/')

    USERNAME_FIELD = 'username'

    objects = UserManager()