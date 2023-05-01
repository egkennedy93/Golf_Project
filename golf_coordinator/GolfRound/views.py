from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DetailView
from GolfRound.forms import scoreform, scoreform_1v1
from GolfRound.models import Round_Score, Net_Round_Score
from golf_trip.models import Trip_TeeTime, Trip_Golfer, Trip_Team, Trip_TeamMember
from bookie.models import GolfBet
from GolfRound.round_processing import round_processing, determine_2v2_team_scores, update_team_scores, viewing_determine_2v2_team_scores, update_player_score, course_handicap_calculation

from bookie.views import bet_processing
from time import sleep

def RoundSubmissionView(request, teetime_pk):
    '''
    This function takes the values submitted for the tee time score, based on the gametype for the teetime.
    it will calculate the raw values, as well as calculate the net data, and ultimiately the team who wins
    '''
    if request.method == "POST":
        teetime_data = get_object_or_404(Trip_TeeTime, pk=teetime_pk)

        if teetime_data.gametype == '1v1 matchplay':
            scoreformset = scoreform_1v1(request.POST)
        else:
            scoreformset = scoreform(request.POST)

        # if data is not properly formatted this will fail. Currently not handling errors for this
        if scoreformset.is_valid():
            
            scoreform_tee_time = scoreformset.save(commit=False)

            # takes all of the round scores from the scoreformset, the information for the teetime (specifically the gametype)
            # reference round_processing.py on the output of round_processing, but its a summary of each players scores - net and gross
            round_score_data = round_processing(scoreformset, teetime_data)


            # have to separate out the net_score players and add them into a list because its easier to work with in the html template
            net_score_list = [] 
            for count,value in enumerate(round_score_data):
                try:
                    player_net = round_score_data[count]['net_score']
                    net_score_list.append(player_net)
                except IndexError:
                    pass

            # for each player in the teetime data, calculate the total gross and net score and replace the default empty field 
            for idx, round in enumerate(scoreform_tee_time):
                round.total_score = sum(round_score_data[idx]['gross_score'])
                round.net_score = sum(round_score_data[idx]['net_score'])
                
            

                # taking data and adding to a net_round_score model so displaying and retrieving the data is easier in the future
                net_round_score = Net_Round_Score.objects.create(tee_time=teetime_data, 
                                                                round_golfer=round.round_golfer,
                                                                hole_1_score = round_score_data[idx]['net_score'][0],
                                                                hole_2_score = round_score_data[idx]['net_score'][1],
                                                                hole_3_score = round_score_data[idx]['net_score'][2],
                                                                hole_4_score = round_score_data[idx]['net_score'][3],
                                                                hole_5_score = round_score_data[idx]['net_score'][4],
                                                                hole_6_score = round_score_data[idx]['net_score'][5],
                                                                hole_7_score = round_score_data[idx]['net_score'][6],
                                                                hole_8_score = round_score_data[idx]['net_score'][7],
                                                                hole_9_score = round_score_data[idx]['net_score'][8],
                                                                hole_10_score = round_score_data[idx]['net_score'][9],
                                                                hole_11_score = round_score_data[idx]['net_score'][10],
                                                                hole_12_score = round_score_data[idx]['net_score'][11],
                                                                hole_13_score = round_score_data[idx]['net_score'][12],
                                                                hole_14_score = round_score_data[idx]['net_score'][13],
                                                                hole_15_score = round_score_data[idx]['net_score'][14],
                                                                hole_16_score = round_score_data[idx]['net_score'][15],
                                                                hole_17_score = round_score_data[idx]['net_score'][16],
                                                                hole_18_score = round_score_data[idx]['net_score'][17],
                                                                net_score = sum(round_score_data[idx]['net_score']),
                                                                total_score = sum(round_score_data[idx]['gross_score']))

            # Using the round_score_data the two team names are passed (which I need to change to be dynamic), and takes in the gametype for the teetime
            processed_score_data = determine_2v2_team_scores(round_score_data, 'Red', 'Blue', teetime_data.gametype)
        scoreformset.save()


        if processed_score_data[2]['net_score'] < 0:
            team = Trip_Team.objects.get(id=processed_score_data[1][0]['team'].values()[0]['id'])
            win_team = get_object_or_404(Trip_Team, pk=team.id)
            win_score = processed_score_data[2]['net_score'] * -1

        elif processed_score_data[2]['net_score'] > 0:
            team = Trip_Team.objects.get(id=processed_score_data[0][0]['team'].values()[0]['id'])
            win_team = get_object_or_404(Trip_Team, pk=team.id)
            win_score = processed_score_data[2]['net_score']

        else:
            win_team = get_object_or_404(Trip_Team, pk=9)
            win_score = 0

        # Trip_TeeTime.objects.filter(pk=teetime_pk).update(teeTime_Complete=True, Winning_Score=winning_score, Winning_Team=winning_team)
        teetime_data.set_winning_score(win_score)
        teetime_data.set_winning_team(win_team)
        teetime_data.complete_round()
        teetime_data.save()

        update_team_scores(processed_score_data[0][0]['team'],processed_score_data[1][0]['team'], processed_score_data[2]['net_score'])
        update_player_score(processed_score_data)

        

        bet_processing(teetime_pk=teetime_data)
        
        # the dictionary paseed is what gets rendered for the html template. Whatever is listed there can be access on the template
        return render(request,'GolfRound/round_submission_POST.html', {'scoreformset': scoreformset, 'teetime_data': teetime_data, 'net_score_list': net_score_list, 'processed_score_data': processed_score_data, 
                                                                        'round_score_data': round_score_data})
# this is the GET request to setup the initial form
    else:

        teetime_data = get_object_or_404(Trip_TeeTime, pk=teetime_pk)

        raw_player_list = teetime_data.Players.all()
        player_list = []
        team_list = []
        player_pks = []
        player_hcp_list = []

        team_1 = []
        team_2 = []

        for player in raw_player_list:
            # This is so when players are displayed in the get view for tee times, they are next to their teammate
            players_team = get_object_or_404(Trip_TeamMember, user=player)
            if players_team.team.id == 7:
                team_1.append(player)
            elif players_team.team.id == 8:
                team_2.append(player)
            player_list = team_1+team_2

        # now that the players have been organized to be by their teammate, need to grab the player meta
        for player in player_list:
            # player_list.append(player)
            team_data = get_object_or_404(Trip_TeamMember, user__golfer__last_name = player.golfer.last_name)
            team_list.append(team_data.team)
            player_hcp_list.append(course_handicap_calculation(player.hcp_index,teetime_data.tee.slope, teetime_data.tee.rating, teetime_data.tee.course_par))
            player_pks.append(player.pk)
        
        try:
            if teetime_data.gametype == '1v1 matchplay':
                scoreformset = scoreform_1v1(queryset=Round_Score.objects.none(), initial=[{'tee_time': teetime_pk, 'round_golfer': player_list[0], 'golfer_index': player_hcp_list[0], 'golfer_pk': player_pks[0]},  
                                                                                {'tee_time': teetime_pk, 'round_golfer': player_list[1], 'golfer_index': player_hcp_list[1], 'golfer_pk': player_pks[1]}, 
                                                                                ])                                                                      
                return render(request, "GolfRound/round_score_submission.html", { 'scoreformset': scoreformset, 'teetime_data': teetime_data })
            else:
                scoreformset = scoreform(queryset=Round_Score.objects.none(), initial=[{'tee_time': teetime_pk, 'round_golfer': player_list[0], 'golfer_index': player_hcp_list[0], 'golfer_pk': player_pks[0]},  
                                                                                    {'tee_time': teetime_pk, 'round_golfer': player_list[1], 'golfer_index': player_hcp_list[1], 'golfer_pk': player_pks[1]}, 
                                                                                    {'tee_time': teetime_pk, 'round_golfer': player_list[2], 'golfer_index': player_hcp_list[2], 'golfer_pk': player_pks[2]}, 
                                                                                    {'tee_time': teetime_pk, 'round_golfer': player_list[3], 'golfer_index': player_hcp_list[3], 'golfer_pk': player_pks[3]},
                                                                                    ])                                                                      
                return render(request, "GolfRound/round_score_submission.html", { 'scoreformset': scoreformset, 'teetime_data': teetime_data })
        except:
            scoreformset = scoreform(queryset=Round_Score.objects.none(), initial=[{'tee_time': teetime_pk, 'round_golfer': "Not Assigned", 'golfer_index': -1, },  
                                                                                {'tee_time': teetime_pk, 'round_golfer': "Not Assigned", 'golfer_index': -1, }, 
                                                                                {'tee_time': teetime_pk, 'round_golfer': "Not Assigned", 'golfer_index': -1, }, 
                                                                                {'tee_time': teetime_pk, 'round_golfer': "Not Assigned", 'golfer_index': -1, },
                                                                                ])
            return render(request, "GolfRound/round_score_submission.html", { 'scoreformset': scoreformset, 'teetime_data': teetime_data })

        


class CompletedRoundView(DetailView):
    model = Trip_TeeTime
    template_name = 'GolfRound/CompletedRoundView_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(CompletedRoundView, self).get_context_data(**kwargs)
        # grabbing the dates for all of the events for the trip
        player_raw_scores = Round_Score.objects.all().filter(tee_time=self.kwargs['pk']).values()
        print(player_raw_scores)
        # grabbing all the courses for the trip
        player_net_scores = Net_Round_Score.objects.all().filter(tee_time=self.kwargs['pk']).values()
        # print(player_net_scores)

        def convert_data_processing_format(player_scores):
            for player in player_scores:
                player_team = Trip_Team.objects.all().filter(members__golfer__last_name=player['round_golfer']).values('team')[0]['team']
                player['team'] = player_team
            return player_scores


        processed_score_data = convert_data_processing_format(player_net_scores)
        scores = viewing_determine_2v2_team_scores(processed_score_data,'Red', 'Blue', context['object'].gametype)
        context['player_raw_scores'] = convert_data_processing_format(player_raw_scores)
        context['player_net_scores'] = player_net_scores
        context['team_1'] = scores[0]
        context['team_2'] = scores[1]
        context['match_results'] = scores[2]
        return context

