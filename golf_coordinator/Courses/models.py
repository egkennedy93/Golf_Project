from django.db import models
from django import template
from django.urls import reverse


# Create your models here.

class Golf_Course(models.Model):
    name = models.CharField(max_length=255, unique=False)

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

class Golf_Round(models.Model):
    course = models.ForeignKey(Golf_Course, related_name='round_course', on_delete=models.CASCADE)
    tee = models.ForeignKey(Golf_Tee, related_name='round_tee', on_delete=models.CASCADE)
    hole_1 = models.ForeignKey(Golf_Hole, related_name='round_hole_1', on_delete=models.CASCADE)
    # hole_2 = ''
    # hole_3 = ''
    # hole_4 = ''
    # hole_5 = ''
    # hole_6 = ''
    # hole_7 = ''
    # hole_8 = ''
    # hole_9 = ''
    # hole_10 = ''
    # hole_11 = ''
    # hole_12 = ''
    # hole_13 = ''
    # hole_14 = ''
    # hole_15 = ''
    # hole_16 = ''
    # hole_17 = ''
    # hole_18 = ''
    class Meta:
        unique_together = ('course', 'tee')

    def __str__(self):
        return "{}_{}_{}".format(self.id, self.course, self.tee)
    