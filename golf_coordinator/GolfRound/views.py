from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView, DetailView
from Courses.models import Golf_Tee
from django.urls import reverse_lazy
from django.forms import formset_factory
from GolfRound.forms import RoundScoreForm, scoreform
from GolfRound.models import Round_Score, Net_Round_Score
from golf_trip.models import Trip_TeeTime, Trip_Golfer
from GolfRound.round_processing import round_processing, determine_2v2_team_scores


def RoundSubmissionView(request, teetime_pk):
    '''
    This function takes the values submitted for the tee time score, based on the gametype for the teetime.
    it will calculate the raw values, as well as calculate the net data, and ultimiately the team who wins
    '''
    if request.method == "POST":
        teetime_data = get_object_or_404(Trip_TeeTime, pk=teetime_pk)
        scoreformset = scoreform(request.POST)

        # if data is not properly formatted this will fail. Currently not handling errors for this
        if scoreformset.is_valid():
            
            scoreform_tee_time = scoreformset.save(commit=False)

             # takes all of the round scores from the scoreformset, the information for the teetime (specifically the gametype)
            # reference round_processing.py on the output of round_processing, but its a summary of each players scores - net and gross
            round_score_data = round_processing(scoreformset, teetime_data)
            print(round_score_data[0]['net_score'][0])


            
            player_0 = round_score_data[0]['net_score']
            player_1 = round_score_data[1]['net_score']
            player_2 = round_score_data[2]['net_score']
            player_3 = round_score_data[3]['net_score']
            net_score_list =[player_0, player_1, player_2, player_3]

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
            # print(processed_score_data)

            scoreformset.save()
            # the dictionary paseed is what gets rendered for the html template. Whatever is listed there can be access on the template
            return render(request,'GolfRound/round_submission_POST.html', {'scoreformset': scoreformset, 'teetime_data': teetime_data, 'net_score_list': net_score_list, 'processed_score_data': processed_score_data})
    else:
        teetime_data = get_object_or_404(Trip_TeeTime, pk=teetime_pk)
        raw_player_list = teetime_data.Players.all()
        player_list = []
        player_pks = []
        player_hcp_list = []

        for player in raw_player_list:
            player_list.append(player)
            player_hcp_list.append(player.hcp_index)
            player_pks.append(player.pk)
        
        scoreformset = scoreform(queryset=Round_Score.objects.none(), initial=[{'tee_time': teetime_pk, 'round_golfer': player_list[0], 'golfer_index': player_hcp_list[0], 'golfer_pk': player_pks[0]},  
                                                                               {'tee_time': teetime_pk, 'round_golfer': player_list[1], 'golfer_index': player_hcp_list[1], 'golfer_pk': player_pks[1]}, 
                                                                               {'tee_time': teetime_pk, 'round_golfer': player_list[2], 'golfer_index': player_hcp_list[2], 'golfer_pk': player_pks[2]}, 
                                                                               {'tee_time': teetime_pk, 'round_golfer': player_list[3], 'golfer_index': player_hcp_list[3], 'golfer_pk': player_pks[3]},
                                                                               ])
        return render(request, "GolfRound/round_score_submission.html", { 'scoreformset': scoreformset, 'teetime_data': teetime_data })
