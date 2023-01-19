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
    round_gametype = models.CharField(max_length=200)
    

class Round_Score(models.Model):
    submission = models.ForeignKey(Round_Submission, related_name='round_submission', on_delete=models.PROTECT)
    round_golfer = models.CharField(max_length=255)
    hole_1_score = models.IntegerField(default=0)
    hole_2_score = models.IntegerField(default=0)
    hole_3_score = models.IntegerField(default=0)

