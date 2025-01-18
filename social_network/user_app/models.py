from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    about_me = models.TextField()
    profile_icon = models.ImageField(upload_to='images/profile_icons', null = True )
