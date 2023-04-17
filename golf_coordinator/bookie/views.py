from django.shortcuts import render
from bookie.models import PlayerVsPlayer, TeamVsTeam
from bookie.forms import BetTeeTimeForm
from django.views.generic import CreateView
from django.shortcuts import get_object_or_404
from golf_trip.models import Trip_TeeTime


# create view to add another tee to a course
class BetPVPCreateView(CreateView):
    model = PlayerVsPlayer
    fields = ('submitter', 'submitter_tee_time','opponent', 'opponent_tee_time', 'units', 'bet_closed',)
    context_object_name = 'player_vs_player'


class BetTVTCreateView(CreateView):
    model = TeamVsTeam
    fields = ('__all__')
    context_object_name = 'team_vs_team'
    


def BetTeeTimeView(request, teetime_pk):
    '''
    This function takes the values submitted for the tee time score, based on the gametype for the teetime.
    it will calculate the raw values, as well as calculate the net data, and ultimiately the team who wins
    '''
    teetime_data = get_object_or_404(Trip_TeeTime, pk=teetime_pk)


    if request.method == "POST":
        
        betteetime = BetTeeTimeForm(request.POST)
        if betteetime.is_valid():
            pass

    elif request.method == "GET":
        form = BetTeeTimeForm(initial=[{'bet_tee_time': 1}])

    context = {'form': form}

    return render(request, "bookie/bet_tee_time.html", context)



# # Create your views here.
# def TeeTimeBetView(request, teetime_pk):

#     if request.method == "POST":
#         teetime_data = get_object_or_404(Trip_TeeTime, pk=teetime_pk)