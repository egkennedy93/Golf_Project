from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User




class Golfer(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    hcp_index = models.DecimalField(max_digits=3, decimal_places=1)
    portfolio = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_pics')

    def __str__(self):
        return self.user.username
    


