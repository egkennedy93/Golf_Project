from django.shortcuts import render
from bookie.models import PlayerVsPlayer, TeamVsTeam
from bookie.forms import BetTeeTimeForm
from django.views.generic import CreateView
from django.shortcuts import get_object_or_404
from golf_trip.models import Trip_TeeTime, Trip_TeamMember, Trip_Team
from GolfRound.round_processing import course_handicap_calculation


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
        
        betteetime = BetTeeTimeForm(request.POST, teetime_pk=teetime_pk)

        print(request.POST)

        if betteetime.is_valid():
            pass
        else:
            print(betteetime.errors)

        betteetime.save()


         # the dictionary paseed is what gets rendered for the html template. Whatever is listed there can be access on the template
        return render(request,'bookie/successful_bet_placed.html', {'betteetime': betteetime, 'teetime_pk': 'teetime_pk'})

    elif request.method == "GET":

        teetime_data = get_object_or_404(Trip_TeeTime, pk=teetime_pk)
        raw_player_list = teetime_data.Players.all()
        player_list = []
        team_list = []
        player_pks = []
        player_hcp_list = []

        team_1_players = []
        team_2_players = []

        
        for player in raw_player_list:
            # This is so when players are displayed in the get view for tee times, they are next to their teammate
            players_team = get_object_or_404(Trip_TeamMember, user=player)
            
            teams = Trip_Team.objects.all().exclude(team='N/A')
            if players_team.team.id == teams[0].id:
                team_1_players.append(player)
            elif players_team.team.id == teams[1].id:
                team_2_players.append(player)
            else:
                raise Exception("player doesn't have a team associated")

            player_list = team_1_players+team_2_players

        # now that the players have been organized to be by their teammate, need to grab the player meta
        for player in player_list:
            # player_list.append(player)
            team_data = get_object_or_404(Trip_TeamMember, user__golfer__last_name = player.golfer.last_name)
            team_list.append(team_data.team)
            player_hcp_list.append(course_handicap_calculation(player.hcp_index,teetime_data.tee.slope, teetime_data.tee.rating, teetime_data.tee.course_par))
            player_pks.append(player.pk)

        form = BetTeeTimeForm(teetime_pk=teetime_pk, initial={'bet_tee_time': teetime_pk})
        teams = Trip_Team.objects.all().filter(trip__trip_name='Michigan')

        try:
            team_1 = teams[0]
            team_2 = teams[1]
        except:
            team_1 = 'N/A'
            team_2 = 'N/A'

        context = {'form': form,
                'team_1': team_1,
                'team_2': team_2,
                'team_1_players': team_1_players,
                'team_2_players': team_2_players,
                'team_list'
                'player_list':player_list,
                }

        return render(request, "bookie/bet_tee_time.html", context)



# # Create your views here.
# def TeeTimeBetView(request, teetime_pk):

#     if request.method == "POST":
#         teetime_data = get_object_or_404(Trip_TeeTime, pk=teetime_pk)