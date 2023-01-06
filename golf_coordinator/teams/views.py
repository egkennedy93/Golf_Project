from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse
from django.views import generic
from teams.models import Team, TeamMember

# Create your views here.


class CreateTeam(LoginRequiredMixin, generic.CreateView):
    fields = ('name', 'description')
    model = Team

class ListTeam(generic.ListView):
    model = Team
