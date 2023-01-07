from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User




class Golfer(models.Model):
    # user = models.OneToOneField(User, on_delete=models.PROTECT)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    hcp_index = models.DecimalField(max_digits=3, decimal_places=1)


    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
    


