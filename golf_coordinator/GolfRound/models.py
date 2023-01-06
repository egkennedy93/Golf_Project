from django.db import models
from django import template
from django.urls import reverse
from Courses.models import Golf_Tee, Golf_Course
from accounts.models import Golfer
from django.utils.timezone import now


# Create your models here.


class Round_Submission(models.Model):
    round_submission_date = models.DateTimeField(default=now())
    course = models.ForeignKey(Golf_Course, on_delete=models.CASCADE)
    tee = models.ForeignKey(Golf_Tee, on_delete=models.CASCADE)
    golfer_1 = models.ForeignKey(Golfer, related_name='player_1', on_delete=models.CASCADE)
    # golfer_2 = models.ForeignKey(Golfer, related_name='player_2', on_delete=models.CASCADE, blank=True)
    # golfer_3 = models.ForeignKey(Golfer, related_name='player_3', on_delete=models.CASCADE, blank=True)
    # golfer_4 = models.ForeignKey(Golfer, related_name='player_4', on_delete=models.CASCADE, blank=True)

    def get_absolute_url(self):
        return reverse("round:round_detail", kwargs={'pk':self.pk})

class Round_Score(models.Model):
    golfer = models.ForeignKey(Golfer, related_name='round_score', on_delete=models.CASCADE)
    hole_1_score = models.IntegerField(default=0)
    hole_2_score = models.IntegerField(default=0)
    hole_3_score = models.IntegerField(default=0)

  


