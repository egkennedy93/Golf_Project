from django.db import models
from django import template
from django.urls import reverse
from Courses.models import Golf_Course, Golf_Tee
from accounts.models import Golfer



# Create your models here.

# core model. Everything else hasa foreign key to this. Intended to be the contianer for all trip related info.
class Golf_Trip(models.Model):
    trip_date = models.DateField()
    trip_name = models.CharField(max_length=255)
    trip_description = models.TextField(max_length=1000)

    def __str__(self):
        return "{}".format(self.trip_name)

# courses and tees need to be loaded in the courses model first, but then is related to a trip.
class Trip_Course(models.Model):
    trip = models.ForeignKey(Golf_Trip, on_delete=models.PROTECT)
    course = models.ForeignKey(Golf_Course, on_delete=models.PROTECT)
    tee = models.ForeignKey(Golf_Tee,  on_delete=models.PROTECT)

    def __str__(self):
        return "{}_{}".format(self.trip.trip_date, self.tee)


# extends the golfer model, and then adds an index and score to each golfer for the trip. 
class Trip_Golfer(models.Model):
    trip = models.ForeignKey(Golf_Trip, on_delete=models.PROTECT)
    golfer = models.ForeignKey(Golfer, on_delete=models.PROTECT)
    hcp_index = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    score = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    bet_winnings = models.DecimalField(max_digits=14, decimal_places=4, null=True, default=0)

    def __str__(self):
        return "{}".format(self.golfer.last_name)
    
    def get_team_object(self):
        return self.trip_team_set.all()


# teams need to be setup first in the team app, but is ued here to track team scores during the trip.
class Trip_Team(models.Model):
    trip = models.ForeignKey(Golf_Trip, on_delete=models.PROTECT)
    team = models.CharField(max_length=255)
    team_score = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    members = models.ManyToManyField(Trip_Golfer, through='Trip_TeamMember')

    def __str__(self):
        return "{}".format(self.team)


class Trip_TeamMember(models.Model):
    team = models.ForeignKey(Trip_Team,on_delete=models.CASCADE)
    user = models.ForeignKey(Trip_Golfer, on_delete=models.CASCADE)

    def __str__(self):
        return "{}_{}_{}".format(self.team.team, self.user.golfer.first_name, self.user.golfer.last_name)
    
    class Meta:
        unique_together = ('team', 'user')


# for each trip events, there wil be multiple tee times to support the trip. This is the sub details on an event.
class Trip_TeeTime(models.Model):
    gametypes = [
    ('2v2 best ball', '2v2 best ball'),
    ('2v2 best ball - matchplay', '2v2 best ball - matchplay'),
    ('2v2 scramble', '2v2 scramble'),
    ('1v1 matchplay', '1v1 matchplay'),
    ('please select', 'please select'),
    ('4 person scramble', '4 person scramble'),
    ]
    
    trip = models.ForeignKey(Golf_Trip, on_delete=models.PROTECT)
    tee_time_date = models.DateField()
    tee_time_time = models.TimeField()
    Players = models.ManyToManyField(Trip_Golfer, blank=True, default="N/A")
    gametype = models.CharField(choices=gametypes, max_length=25, default=gametypes[4][1])
    tee = models.ForeignKey(Golf_Tee,  on_delete=models.PROTECT)
    teeTime_Complete = models.BooleanField(default=False)
    Winning_Score = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    Winning_Team = models.ForeignKey(Trip_Team, on_delete=models.PROTECT)

    def bets(self):
        return self.golfbet_tee_time.all()
    
    def net_rounds(self):
        return self.net_round_score_set.all()
        

    


# Trip event is ment to be each round of golf. This can occur multipel times on the same day. 
class Trip_Event(models.Model):
    trip = models.ForeignKey(Golf_Trip, on_delete=models.PROTECT)
    event_time = models.DateField()
    course = models.ForeignKey(Trip_Course, on_delete=models.PROTECT)
    tee_time=models.ManyToManyField(Trip_TeeTime, null=True, blank=True)

    def __str__(self):
        return "{}_{}_{}".format(self.trip, self.tee_time, self.course)



