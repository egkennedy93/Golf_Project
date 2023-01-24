from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView, DetailView
from Courses.models import Golf_Tee
from django.urls import reverse_lazy
from django.forms import formset_factory
from GolfRound.forms import RoundScoreForm, scoreform
from GolfRound.models import Round_Score
from golf_trip.models import Trip_TeeTime



def RoundSubmissionView(request, teetime_pk):
    # inlineformet is being used to update the Golf_Tee and Golf_Course under the same form POST 
    # TeeFormSet = inlineformset_factory(Golf_Course, Golf_Tee, form=AddTeeForm, extra=1,)
    if request.method == "POST":
        scoreformset = scoreform(request.POST)

        if scoreformset.is_valid():
            scoreform_tee_time = scoreformset.save(commit=False)
            # for i in scoreformset:
                # print(i.cleaned_data['round_golfer'])


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
