from django.db import models
from django import template
from django.urls import reverse
from Courses.models import Golf_Tee
from accounts.models import Golfer
from django.utils.timezone import now


# Create your models here.

class Golf_Round(models.Model):
    is_active_round = models.BooleanField(default=False)
    round_create_date = models.DateTimeField(default=now())
    tee = models.ForeignKey(Golf_Tee, on_delete=models.CASCADE)
    course = models.ForeignKey(Golf_Tee, to_field='course', related_name="round_cource", unique=True, on_delete=models.CASCADE)

    def __str__(self):
        return "{}.{}.{}.{}".format(self.id, self.tee.course, self.tee.tee_name, self.round_create_date)


class Round_Hole_Player(models.Model):
    round = models.ForeignKey(Golf_Round, to_field='id' ,on_delete=models.CASCADE)
    player = models.ForeignKey(Golfer, on_delete=models.CASCADE)
    hole_1_score = models.IntegerField(default=0, blank=True)
    hole_2_score = models.IntegerField(default=0, blank=True)
    hole_3_score = models.IntegerField(default=0, blank=True)
    hole_4_score = models.IntegerField(default=0, blank=True)
    hole_5_score = models.IntegerField(default=0, blank=True)
    hole_6_score = models.IntegerField(default=0, blank=True)
    hole_7_score = models.IntegerField(default=0, blank=True)
    hole_8_score = models.IntegerField(default=0, blank=True)
    hole_9_score = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return "{}.{}".format(self.round, self.player)


