from django.db import models
from django import template
from django.urls import reverse
from Courses.models import Golf_Tee, Golf_Course
from accounts.models import Golfer
from django.utils.timezone import now


# Create your models here.

class Golf_Round(models.Model):
    is_active_round = models.BooleanField(default=False)
    round_create_date = models.DateTimeField(default=now())
    course = models.CharField(max_length=255) 
    tee = models.ForeignKey(Golf_Tee, on_delete=models.CASCADE)
    player_1 = models.ForeignKey(Golfer, on_delete=models.CASCADE)
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
        return "{}.{}.{}.{}".format(self.id, self.tee.course, self.tee.tee_name, self.round_create_date)


class Round_Submission(models.Model):
    course = models.CharField(max_length=255)
    round_submission_date = models.DateTimeField(default=now())
    tee = models.ForeignKey(Golf_Tee, on_delete=models.CASCADE)
    golfer_1 = models.ForeignKey(Golfer, related_name='player_1', on_delete=models.CASCADE)
    # golfer_2 = models.ForeignKey(Golfer, related_name='player_2', on_delete=models.CASCADE, blank=True)
    # golfer_3 = models.ForeignKey(Golfer, related_name='player_3', on_delete=models.CASCADE, blank=True)
    # golfer_4 = models.ForeignKey(Golfer, related_name='player_4', on_delete=models.CASCADE, blank=True)

