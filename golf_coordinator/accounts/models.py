from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User



# Model that extends the contrib.auth package to support golfer specific attributes.
# after developing more, it made more sense to have handicaps associated with the trip, and not the user model. Might have a overall 
# handicap at a later date 
class Golfer(models.Model):
    # user = models.OneToOneField(User, on_delete=models.PROTECT)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)


    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
    


