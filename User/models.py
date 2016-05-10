from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):  #UserProfile is an extension of User
    user = models.OneToOneField(User)
    alias = models.CharField(max_length=50)
    #image = models.ImageField()

    def __str__(self):
        return str(self.user)