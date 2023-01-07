from django.db import models
from django.contrib.auth import get_user_model
from django import template
from django.urls import reverse
from accounts.models import Golfer
# Create your models here.

User = get_user_model()
register = template.Library()

class Team(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, default='')
    members = models.ManyToManyField(Golfer, through='TeamMember')
    team_score = models.DecimalField(max_digits=3, decimal_places=1, default=0)


    def __str__(self):
        return self.name
        
    def save(self, *args, **kwargs):
        pass

    def get_absolute_url(self):
        return reverse('teams:single', kwargs={'name':self.name})
    
    class Meta:
        ordering = ['name']


class TeamMember(models.Model):
    team = models.ForeignKey(Team, related_name='memberships',on_delete=models.CASCADE)
    user = models.ForeignKey(Golfer, related_name='user_teams', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    
    class Meta:
        unique_together = ('team', 'user')