from django.db import models
from django import template
from django.urls import reverse


# Create your models here.

class Golf_Course(models.Model):
    name = models.CharField(max_length=255, unique=False)
    tee = models.ForeignKey('Golf_Tee', related_name='course_tee', on_delete=models.CASCADE, default="")

    def __str__(self):
        return self.name


class Golf_Tee(models.Model):
    course = models.ForeignKey(Golf_Course, related_name='tee_course', on_delete=models.CASCADE)
    tee_color = models.CharField(max_length=25, unique=True)
    tee_name = models.CharField(max_length=25, unique=True)
    par = models.IntegerField()
    slope = models.FloatField()
    rating = models.FloatField()
    yardage = models.IntegerField()

    class Meta:
        unique_together = ('course', 'tee_color')

    def __str__(self):
        return "{}_{}".format(self.course, self.tee_name)


class Golf_Hole(models.Model):
    course = models.ForeignKey(Golf_Course, related_name='hole_course', on_delete=models.CASCADE)
    tee = models.ForeignKey(Golf_Tee, related_name='hole_tee', on_delete=models.CASCADE)
    hole_number = models.IntegerField()
    par = models.IntegerField()
    yardage = models.IntegerField()
    hcp_index = models.IntegerField()

    class Meta:
        unique_together = ('course', 'tee', 'hole_number')

    def __str__(self):
        return "{}_{}_{}".format(self.course, self.tee, self.hole_number) 
