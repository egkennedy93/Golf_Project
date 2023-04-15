from django.shortcuts import render
from bookie.models import PlayerVsPlayer, TeamVsTeam
from django.views.generic import CreateView

# create view to add another tee to a course
class BetPVPCreateView(CreateView):
    model = PlayerVsPlayer
    fields = ('submitter', 'submitter_tee_time','opponent', 'opponent_tee_time', 'units', 'bet_closed',)
    context_object_name = 'player_vs_player'


class BetTVTCreateView(CreateView):
    model = TeamVsTeam
    fields = ('__all__')
    context_object_name = 'team_vs_team'
    



# # Create your views here.
# def TeeTimeBetView(request, teetime_pk):

#     if request.method == "POST":
#         teetime_data = get_object_or_404(Trip_TeeTime, pk=teetime_pk)