from django.db import models
from django import template
from django.urls import reverse


# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=255, unique=False)
    tee = ''


class Golf_Tee(models.Model):
    course = ''
    color = ''
    name = ''
    par = ''
    slope = ''
    rating = ''
    yardage = ''


class Golf_Hole(models.Model):
    course = ''
    tee = ''
    hole_number = ''
    par = ''
    yardage = ''
    Index = ''
