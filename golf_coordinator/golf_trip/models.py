from django.db import models
from django import template
from django.urls import reverse
from teams.models import Team
from Courses.models import Golf_Course, Golf_Tee
from accounts.models import Golfer


# Create your models here.

class Golf_Trip(models.Model):
    trip_date = models.DateField()
    trip_name = models.CharField(max_length=255)
    trip_description = models.TextField(max_length=1000)

    def __str__(self):
        return "{}".format(self.trip_name)


class Trip_Course(models.Model):
    trip = models.ForeignKey(Golf_Trip, on_delete=models.PROTECT)
    course = models.ForeignKey(Golf_Course, on_delete=models.PROTECT)
    tee = models.ForeignKey(Golf_Tee,  on_delete=models.PROTECT)

    def __str__(self):
        return "{}_{}".format(self.trip.trip_date, self.tee)


class Trip_Team(models.Model):
    trip = models.ForeignKey(Golf_Trip, on_delete=models.PROTECT)
    team = models.ForeignKey(Team, on_delete=models.PROTECT)
    team_score = models.DecimalField(max_digits=3, decimal_places=1, default=0)

    def __str__(self):
        return "{}_{}".format(self.trip, self.team)


class Trip_Golfer(models.Model):
    trip = models.ForeignKey(Golf_Trip, on_delete=models.PROTECT)
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.PROTECT)
    golfer = models.ForeignKey(Golfer, on_delete=models.PROTECT)
    hcp_index = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    score = models.DecimalField(max_digits=3, decimal_places=1, default=0)

    def __str__(self):
        return "{}_{}".format(self.trip, self.golfer)


class Trip_TeeTime(models.Model):
    trip = models.ForeignKey(Golf_Trip, on_delete=models.PROTECT)
    tee_time = models.DateTimeField()
    Players = models.ManyToManyField(Trip_Golfer)
    tee = models.ForeignKey(Golf_Tee,  on_delete=models.PROTECT)

class Trip_Event(models.Model):
    trip = models.ForeignKey(Golf_Trip, on_delete=models.PROTECT)
    event_time = models.DateField()
    course = models.ForeignKey(Trip_Course, on_delete=models.PROTECT)
    tee_time=models.ManyToManyField(Trip_TeeTime, null=True, blank=True)

    def __str__(self):
        return "{}_{}_{}".format(self.trip, self.tee_time, self.course)



