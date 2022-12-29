from django.db import models
from django import template
from django.urls import reverse


# Create your models here.

class Golf_Course(models.Model):
    course_name = models.CharField(max_length=255, unique=False)

    def __str__(self):
        return "{}".format(self.course_name)


class Golf_Tee(models.Model):
    INDEX = [
    ('1', 1),
    ('2', 2),
    ('3', 3),
    ('4', 4),
    ('5', 5),
    ('6', 6),
    ('7', 7),
    ('8', 8),
    ('9', 9),
    ('10', 10),
    ('11', 11),
    ('12', 12),
    ('13', 13),
    ('14', 14),
    ('15', 15),
    ('16', 16),
    ('17', 17),
    ('18', 18),
    ]

    PAR = [
    ('3', 3),
    ('4', 4),
    ('5', 5),
    ]

    course_name = models.ForeignKey(Golf_Course, on_delete=models.CASCADE)
    tee_name = models.CharField(max_length=255, unique=True)
    course_par = models.IntegerField()
    slope = models.DecimalField(decimal_places=2, max_digits=5)
    rating = models.DecimalField(decimal_places=2, max_digits=5)
    yardage = models.IntegerField()
    hole_1_par = models.IntegerField(choices=PAR, default = 4)
    hole_1_yardage = models.IntegerField(default = 0)
    hole_1_index = models.IntegerField(choices=INDEX, default=1)

    hole_2_par = models.IntegerField(choices=PAR, default = 4)
    hole_2_yardage = models.IntegerField(default = 0)
    hole_2_index = models.IntegerField(choices=INDEX, default=1)

    hole_3_par = models.IntegerField(choices=PAR, default = 4)
    hole_3_yardage = models.IntegerField(default = 0)
    hole_3_index = models.IntegerField(choices=INDEX, default=1)

    hole_4_par = models.IntegerField(choices=PAR, default = 4)
    hole_4_yardage = models.IntegerField(default = 0)
    hole_4_index = models.IntegerField(choices=INDEX, default=1)

    hole_5_par = models.IntegerField(choices=PAR, default = 4)
    hole_5_yardage = models.IntegerField(default = 0)
    hole_5_index = models.IntegerField(choices=INDEX, default=1)

    hole_6_par = models.IntegerField(choices=PAR, default = 4)
    hole_6_yardage = models.IntegerField(default = 0)
    hole_6_index = models.IntegerField(choices=INDEX, default=1)

    hole_7_par = models.IntegerField(choices=PAR, default = 4)
    hole_7_yardage = models.IntegerField(default = 0)
    hole_7_index = models.IntegerField(choices=INDEX, default=1)

    hole_8_par = models.IntegerField(choices=PAR, default = 4)
    hole_8_yardage = models.IntegerField(default = 0)
    hole_8_index = models.IntegerField(choices=INDEX, default=1)

    hole_9_par = models.IntegerField(choices=PAR, default = 4)
    hole_9_yardage = models.IntegerField(default = 0)
    hole_9_index = models.IntegerField(choices=INDEX, default=1)

    hole_10_par = models.IntegerField(choices=PAR, default = 4)
    hole_10_yardage = models.IntegerField(default = 0)
    hole_10_index = models.IntegerField(choices=INDEX, default=1)

    hole_11_par = models.IntegerField(choices=PAR, default = 4)
    hole_11_yardage = models.IntegerField(default = 0)
    hole_11_index = models.IntegerField(choices=INDEX, default=1)

    hole_12_par = models.IntegerField(choices=PAR, default = 4)
    hole_12_yardage = models.IntegerField(default = 0)
    hole_12_index = models.IntegerField(choices=INDEX, default=1)

    hole_13_par = models.IntegerField(choices=PAR, default = 4)
    hole_13_yardage = models.IntegerField(default = 0)
    hole_13_index = models.IntegerField(choices=INDEX, default=1)

    hole_14_par = models.IntegerField(choices=PAR, default = 4)
    hole_14_yardage = models.IntegerField(default = 0)
    hole_14_index = models.IntegerField(choices=INDEX, default=1)

    hole_15_par = models.IntegerField(choices=PAR, default = 4)
    hole_15_yardage = models.IntegerField(default = 0)
    hole_15_index = models.IntegerField(choices=INDEX, default=1)

    hole_16_par = models.IntegerField(choices=PAR, default = 4)
    hole_16_yardage = models.IntegerField(default = 0)
    hole_16_index = models.IntegerField(choices=INDEX, default=1)

    hole_17_par = models.IntegerField(choices=PAR, default = 4)
    hole_17_yardage = models.IntegerField(default = 0)
    hole_17_index = models.IntegerField(choices=INDEX, default=1)

    hole_18_par = models.IntegerField(choices=PAR, default = 4)
    hole_18_yardage = models.IntegerField(default = 0)
    hole_18_index = models.IntegerField(choices=INDEX, default=1)
    class Meta:
        unique_together = ('course_name', 'tee_name',)

    def __str__(self):
        return "{}_{}".format(self.course_name, self.tee_name) 
    
      