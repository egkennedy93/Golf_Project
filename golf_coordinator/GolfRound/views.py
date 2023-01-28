from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView, DetailView
from Courses.models import Golf_Tee
from django.urls import reverse_lazy
from django.forms import formset_factory
from GolfRound.forms import RoundScoreForm, scoreform
from GolfRound.models import Round_Score, Net_Round_Score
from golf_trip.models import Trip_TeeTime
from GolfRound.round_processing import round_processing, determine_2v2_team_scores





def RoundSubmissionView(request, teetime_pk):
    if request.method == "POST":
        teetime_data = get_object_or_404(Trip_TeeTime, pk=teetime_pk)
        scoreformset = scoreform(request.POST)
    
        if scoreformset.is_valid():
            
            round_score_data = round_processing(scoreformset, teetime_data, teetime_data)
            processed_score_data = determine_2v2_team_scores(round_score_data, 'Red', 'Blue', teetime_data.gametype)

            scoreform_tee_time = scoreformset.save(commit=False)

            for golfer in round_score_data:
                print(golfer['gross_score'])
                print(golfer['net_score'])
                # scoreform_tee_time.total_score = golfer['gross_score']
                # scoreform_tee_time.net_score = golfer['net_score']
                # print(scoreform_tee_time.total_score)

            scoreform_tee_time.save()
            # the dictionary paseed is what gets rendered for the html template. Whatever is listed there can be access on the template
            return render(request,'GolfRound/round_submission_POST.html', {'scoreform_tee_time': scoreform_tee_time})
    else:
        teetime_data = get_object_or_404(Trip_TeeTime, pk=teetime_pk)
        player_list = []
        player_hcp_list = []

        for player in teetime_data.Players.all():
            player_name = "{}".format(player.golfer.last_name)
            player_hcp = "{}".format(player.hcp_index)
            player_list.append(player_name)
            player_hcp_list.append(player_hcp)

        scoreformset = scoreform(queryset=Round_Score.objects.none(), initial=[{'tee_time': teetime_pk, 'round_golfer': player_list[0], 'golfer_index': player_hcp_list[0]},  
                                                                               {'tee_time': teetime_pk, 'round_golfer': player_list[1], 'golfer_index': player_hcp_list[1]}, 
                                                                               {'tee_time': teetime_pk, 'round_golfer': player_list[2], 'golfer_index': player_hcp_list[2]}, 
                                                                               {'tee_time': teetime_pk, 'round_golfer': player_list[3], 'golfer_index': player_hcp_list[3]},
                                                                               ])
        return render(request, "GolfRound/round_score_submission.html", { 'scoreformset': scoreformset, 'teetime_data': teetime_data })
