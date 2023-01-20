from django.db import models
from django.urls import reverse
from Courses.models import Golf_Tee, Golf_Course
from accounts.models import Golfer
from golf_trip.models import Trip_TeeTime, Trip_Golfer
from django.utils.timezone import now


# Create your models here.
class Round_Submission(models.Model):
    round_submission_date = models.DateTimeField(default=now())
    trip_teetime = models.ForeignKey(Trip_TeeTime, on_delete=models.PROTECT)
    

class Round_Score(models.Model):
    submission = models.ForeignKey(Round_Submission, on_delete=models.PROTECT)
    round_golfer = models.CharField(max_length=255)
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
    total_score = models.IntegerField()
    net_score = models.IntegerField()

