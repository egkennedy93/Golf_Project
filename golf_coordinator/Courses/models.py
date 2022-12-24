from django.db import models
from django import template
from django.urls import reverse


# Create your models here.

class Golf_Course(models.Model):
    course_name = models.CharField(max_length=255, unique=False)
    tee_name = models.CharField(max_length=255, unique=False)

    def __str__(self):
        return "{}".format(self.course_name)

class Golf_Hole(models.Model):
    course_name = models.ForeignKey(Golf_Course, related_name='hole_course', on_delete=models.CASCADE)
    referred_tee_name = models.ForeignKey(Golf_Course, related_name='hole_tee', on_delete=models.CASCADE)
    hole_number = models.IntegerField()
    par = models.IntegerField()
    yardage = models.IntegerField()
    hcp_index = models.IntegerField()

    class Meta:
        unique_together = ('course_name', 'referred_tee_name', 'hole_number')
        

    def __str__(self):
        return "{}_{}_{}".format(self.course_name, self.referred_tee_name, self.hole_number) 


class Golf_Tee(models.Model):
    course_name = models.ForeignKey(Golf_Course, related_name='tee_course_name', on_delete=models.CASCADE)
    tee_name = models.ForeignKey(Golf_Course, related_name='tee_name_from_course', on_delete=models.CASCADE)
    par = models.IntegerField()
    slope = models.DecimalField(decimal_places=2, max_digits=5)
    rating = models.DecimalField(decimal_places=2, max_digits=5)
    yardage = models.IntegerField()
    hole_1 = models.ForeignKey(Golf_Hole, related_name='tee_hole_2', on_delete=models.CASCADE)
    hole_2 = models.ForeignKey(Golf_Hole, related_name='tee_hole_3', on_delete=models.CASCADE)
    hole_3 = models.ForeignKey(Golf_Hole, related_name='tee_hole_4', on_delete=models.CASCADE)
    hole_5 = models.ForeignKey(Golf_Hole, related_name='tee_hole_5', on_delete=models.CASCADE)
    hole_6 = models.ForeignKey(Golf_Hole, related_name='tee_hole_6', on_delete=models.CASCADE)
    hole_7 = models.ForeignKey(Golf_Hole, related_name='tee_hole_7', on_delete=models.CASCADE)
    hole_8 = models.ForeignKey(Golf_Hole, related_name='tee_hole_8', on_delete=models.CASCADE)
    hole_9 = models.ForeignKey(Golf_Hole, related_name='tee_hole_9', on_delete=models.CASCADE)
    hole_10 = models.ForeignKey(Golf_Hole, related_name='tee_hole_10', on_delete=models.CASCADE)
    hole_11 = models.ForeignKey(Golf_Hole, related_name='tee_hole_11', on_delete=models.CASCADE)
    hole_12 = models.ForeignKey(Golf_Hole, related_name='tee_hole_12', on_delete=models.CASCADE)
    hole_13 = models.ForeignKey(Golf_Hole, related_name='tee_hole_13', on_delete=models.CASCADE)
    hole_14 = models.ForeignKey(Golf_Hole, related_name='tee_hole_14', on_delete=models.CASCADE)
    hole_15 = models.ForeignKey(Golf_Hole, related_name='tee_hole_15', on_delete=models.CASCADE)
    hole_16 = models.ForeignKey(Golf_Hole, related_name='tee_hole_16', on_delete=models.CASCADE)
    hole_17 = models.ForeignKey(Golf_Hole, related_name='tee_hole_17', on_delete=models.CASCADE)
    hole_18 = models.ForeignKey(Golf_Hole, related_name='tee_hole_18', on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('course_name', 'tee_name',)

    def __str__(self):
        return "{}_{}".format(self.course_name, self.tee_name)




class New_Course_Entry(models.Model):
    # course_name = ''
    # course_tee = ''
    # course_tee_color = ''
    # course_par = ''
    # course_slope = ''
    # course_rating = ''
    # course_yardage = ''
    
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
    # class Meta:
    #     unique_together = ('course_name', 'course_tee')

    def __str__(self):
        return "{}_{}_{}".format(self.id, self.course, self.tee)
    