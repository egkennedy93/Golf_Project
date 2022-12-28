from django.db import models
from django import template
from django.urls import reverse


# Create your models here.

class Golf_Course(models.Model):
    golf_course_id = models. AutoField(primary_key=True)
    course_name = models.CharField(max_length=255, unique=False)

    def __str__(self):
        return "{}".format(self.course_name)


class Golf_Tee(models.Model):
    course_name = models.ForeignKey(Golf_Course, on_delete=models.CASCADE)
    tee_name = models.CharField(max_length=255, unique=True)
    course_par = models.IntegerField()
    slope = models.DecimalField(decimal_places=2, max_digits=5)
    rating = models.DecimalField(decimal_places=2, max_digits=5)
    yardage = models.IntegerField()
   
    class Meta:
        unique_together = ('course_name', 'tee_name',)

    def __str__(self):
        return "{}_{}".format(self.course_name, self.tee_name) 

class Golf_Hole(models.Model):
    tee_name = models.ForeignKey(Golf_Tee, on_delete=models.CASCADE)
    hole_number = models.IntegerField()
    par = models.IntegerField()
    yardage = models.IntegerField()
    hcp_index = models.IntegerField()

    class Meta:
        unique_together = ('tee_name', 'hole_number')
        

    def __str__(self):
        return "{}_{}".format(self.tee_name, self.hole_number) 
    
      