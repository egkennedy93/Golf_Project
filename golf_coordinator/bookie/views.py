from django.shortcuts import render
from bookie.models import TeamVsTeam, GolfBet
from bookie.forms import BetTeeTimeForm
from django.views.generic import CreateView, ListView
from django.shortcuts import get_object_or_404
from golf_trip.models import Trip_TeeTime, Trip_TeamMember, Trip_Team, Trip_Golfer, Trip_Event
from GolfRound.round_processing import course_handicap_calculation
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages


class GolfBetListView(ListView):
    model = GolfBet

    def get_context_data(self, **kwargs):
        context = super(GolfBetListView, self).get_context_data(**kwargs)
        context['trip'] = Trip_Event.objects.all().filter(trip__trip_name='Michigan')
        return context
    

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


        if betteetime.is_valid():
            pass
        else:
            print(betteetime.errors)

        betteetime.save()


         # the dictionary paseed is what gets rendered for the html template. Whatever is listed there can be access on the template
        # return render(request, 'golf_trip/trip_event_list.html', {'bet': teetime_data.tee_time_date})
        messages.success(request, "Your bet has been placed!")
        return HttpResponseRedirect(reverse('golf_trip:event_teetime', kwargs={'event_day': teetime_data.tee_time_date}),{'redirect': True})
        # return render(request,'bookie/successful_bet_placed.html', {'betteetime': betteetime, 'teetime_pk': 'teetime_pk'})

    elif request.method == "GET":


        teetime_data = get_object_or_404(Trip_TeeTime, pk=teetime_pk)
        raw_player_list = teetime_data.Players.all()
        player_list = []
        team_list = []
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
            # player_pks.append(player.pk)

        form = BetTeeTimeForm(teetime_pk=teetime_pk, initial={'bet_tee_time': teetime_pk})
        
        # Since the opponent field needs to be filtered down to just the associated teetime's players the players pks need to be queried
        opponent_players = Trip_TeeTime.objects.filter(pk=teetime_pk).values_list('Players', flat=True)

        #to filter down the opponent list, a queryset is created and is filtering on if the PK is in the opponent_players list
        form.fields['opponent'].queryset = Trip_Golfer.objects.all().filter(pk__in=list(opponent_players))

        #setting the teetime_PK for the hidden bet_tee_time input
        form.fields['bet_tee_time'].queryset = Trip_TeeTime.objects.filter(pk=teetime_pk)

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
    
def bet_processing(teetime_pk):


    # checking to make sure the teetime is finished
    if teetime_pk.teeTime_Complete:
        print("complete")

        # grabbing all of the bets associated with the teetime object
        teetime_bets = teetime_pk.bets()

        for bet in teetime_bets:
            # if bet is equal to 'bet against player'
            if bet.bet_type == '1':
                submitter = bet.submitter
                opponent = bet.opponent

                # checking if the submitter is in the teetime
                if submitter in teetime_pk.Players.all(): 
                    print("submitter in teetime")
                    # grabbing all the net_scores for the teetime
                    teetime_net_scores = teetime_pk.net_rounds()
                    
                    submitter_net_score = teetime_net_scores.filter(round_golfer=submitter.full_name()).values()[0]
                    opponent_net_score = teetime_net_scores.filter(round_golfer=opponent.full_name()).values()[0]

                    if submitter_net_score['net_score'] < opponent_net_score['net_score']:
                        
                        bet.bet_winner = submitter
                        submitter.distribute_units(bet.units)
                        opponent.distribute_units((-1*bet.units))
                        bet.bet_closed = True

                        bet.save()
                        submitter.save()
                        opponent.save()

                    if opponent_net_score['net_score'] < submitter_net_score['net_score']:
                        bet.bet_winner = opponent
                        opponent.distribute_units(bet.units)
                        submitter.distribute_units((-1*bet.units))
                        bet.bet_closed = True

                        bet.save()
                        submitter.save()
                        opponent.save()
                        
                    else:
                       bet.bet_closed = True
                       bet.save()
                else:
                    # get the teetime associated with that submitter for the day
                    submitter_tee_time = Trip_TeeTime.objects.all().filter(tee__course__course_name=bet.bet_tee_time.tee.course.course_name).filter(Players=submitter).get()
                    if submitter_tee_time.teeTime_Complete == True and teetime_pk.teeTime_Complete == True:
                        submitter_net_scores = submitter_tee_time.net_rounds()
                        opponent_net_scores = teetime_pk.net_rounds()
                        
                        submitter_net_score = submitter_net_scores.filter(round_golfer=submitter.full_name()).values()[0]
                        opponent_net_score = opponent_net_scores.filter(round_golfer=opponent.full_name()).values()[0]


                        if submitter_net_score['net_score'] < opponent_net_score['net_score']:
                            
                            bet.bet_winner = submitter
                            submitter.distribute_units(bet.units)
                            opponent.distribute_units((-1*bet.units))
                            bet.bet_closed = True

                            bet.save()
                            submitter.save()
                            opponent.save()

                        if opponent_net_score['net_score'] < submitter_net_score['net_score']:
                            bet.bet_winner = opponent
                            opponent.distribute_units(bet.units)
                            submitter.distribute_units((-1*bet.units))
                            bet.bet_closed = True

                            bet.save()
                            submitter.save()
                            opponent.save()
                            
                    else:
                        bet.bet_closed = False
                        bet.save()

                

            # if bet is equal to 'bet against team'
            if bet.bet_type == '2':
                pass
    else:
        print('error. Teetime hasnt been completed yet')

        

