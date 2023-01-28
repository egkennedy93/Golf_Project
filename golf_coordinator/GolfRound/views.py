from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView, DetailView
from Courses.models import Golf_Tee
from django.urls import reverse_lazy
from django.forms import formset_factory
from GolfRound.forms import RoundScoreForm, scoreform
from GolfRound.models import Round_Score
from golf_trip.models import Trip_TeeTime
from GolfRound.round_processing import round_processing





def RoundSubmissionView(request, teetime_pk):
    if request.method == "POST":
        teetime_data = get_object_or_404(Trip_TeeTime, pk=teetime_pk)
        scoreformset = scoreform(request.POST)

        if scoreformset.is_valid():
            # print(scoreform_tee_time)
            round_score_data = round_processing(scoreformset, teetime_data, teetime_data)

            scoreform_tee_time = scoreformset.save(commit=False)
            

            scoreformset.save()
            # the dictionary paseed is what gets rendered for the html template. Whatever is listed there can be access on the template
            return render(request,'GolfRound/round_submission_POST.html', {'scoreformset': scoreformset})
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
