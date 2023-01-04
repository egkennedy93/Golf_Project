from django.db import models
from django import template
from django.urls import reverse
from Courses.models import Golf_Course
from accounts.models import Golfer
from django.utils.timezone import now


# Create your models here.

class Golf_Round(models.Model):
    course = models.ForeignKey(Golf_Course, on_delete=models.CASCADE)
    round_create_date = models.DateTimeField(default=now())
    is_active_round = models.BooleanField(default=False)

    def __str__(self):
        return "{}.{}.{}".format(self.round_create_date, self.course,self.pk)

class Round_Player(models.Model):
    player = models.ForeignKey(Golfer, on_delete=models.CASCADE, default='Please_Select',blank=False)
    round = models.ForeignKey(Golf_Round, on_delete=models.CASCADE)
    hole_1_score = models.IntegerField()
    hole_2_score = models.IntegerField()
    hole_3_score = models.IntegerField()
    hole_4_score = models.IntegerField()
    hole_5_score = models.IntegerField()
    hole_6_score = models.IntegerField()
    hole_7_score = models.IntegerField()
    hole_8_score = models.IntegerField()
    hole_9_score = models.IntegerField()
    hole_10_score = models.IntegerField()
    hole_11_score = models.IntegerField()
    hole_12_score = models.IntegerField()
    hole_13_score = models.IntegerField()
    hole_14_score = models.IntegerField()
    hole_15_score = models.IntegerField()
    hole_16_score = models.IntegerField()
    hole_17_score = models.IntegerField()
    hole_18_score = models.IntegerField()

    create_date = models.DateTimeField(default=now())

    def __str__(self):
        return "{}.{}.{}".format(self.round_create_date, self.player, self.course)

