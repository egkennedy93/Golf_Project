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
    if request.method == "POST":
        print(request)
        teetime_data = get_object_or_404(Trip_TeeTime, pk=teetime_pk)
        scoreformset = scoreform(request.POST)
    
        if scoreformset.is_valid():
            
            round_score_data = round_processing(scoreformset, teetime_data, teetime_data)
            processed_score_data = determine_2v2_team_scores(round_score_data, 'Red', 'Blue', teetime_data.gametype)

            scoreform_tee_time = scoreformset.save(commit=False)

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
            scoreformset.save()
            # the dictionary paseed is what gets rendered for the html template. Whatever is listed there can be access on the template
            return render(request,'GolfRound/round_submission_POST.html', {'scoreform_tee_time': scoreform_tee_time, 'net_round_score': net_round_score})
    else:
        teetime_data = get_object_or_404(Trip_TeeTime, pk=teetime_pk)
        raw_player_list = teetime_data.Players.all()
        player_list = []
        player_pks = []
        player_hcp_list = []


        for player in teetime_data.Players.all():
            player_name = "{}".format(player.golfer.last_name)
            player_hcp = "{}".format(player.hcp_index)
            player_list.append(player_name)
            player_hcp_list.append(player_hcp)
            player_pks.append(player.pk)

        scoreformset = scoreform(queryset=Round_Score.objects.none(), initial=[{'tee_time': teetime_pk, 'round_golfer': raw_player_list[0], 'golfer_index': player_hcp_list[0], 'golfer_pk': player_pks[0]},  
                                                                               {'tee_time': teetime_pk, 'round_golfer': raw_player_list[1], 'golfer_index': player_hcp_list[1], 'golfer_pk': player_pks[1]}, 
                                                                               {'tee_time': teetime_pk, 'round_golfer': raw_player_list[2], 'golfer_index': player_hcp_list[2], 'golfer_pk': player_pks[2]}, 
                                                                               {'tee_time': teetime_pk, 'round_golfer': raw_player_list[3], 'golfer_index': player_hcp_list[3], 'golfer_pk': player_pks[3]},
                                                                               ])
        return render(request, "GolfRound/round_score_submission.html", { 'scoreformset': scoreformset, 'teetime_data': teetime_data })
