from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView, DetailView
from Courses.models import Golf_Tee
from django.urls import reverse_lazy
from django.forms import inlineformset_factory
from GolfRound.forms import RoundSubmissionForm, RoundScoreForm
from GolfRound.models import Round_Submission
from golf_trip.models import Trip_TeeTime



def RoundSubmissionView(request, teetime_pk):
    # inlineformet is being used to update the Golf_Tee and Golf_Course under the same form POST 
    # TeeFormSet = inlineformset_factory(Golf_Course, Golf_Tee, form=AddTeeForm, extra=1,)
    if request.method == "POST":
        submission_form = RoundSubmissionForm(request.POST)
        score_form = RoundScoreForm(request.POST)
                
        
        # the dictionary paseed is what gets rendered for the html template. Whatever is listed there can be access on the template
        return render(request,'GolfRound/round_submission_POST.html',{'submission_form': submission_form.cleaned_data})
    elif request.method == "GET":
        teetime_data = get_object_or_404(Trip_TeeTime, pk=teetime_pk)
        submission_form = RoundSubmissionForm()
        score_form = RoundScoreForm()
        # teeformset = TeeFormSet()
    return render(request, "GolfRound/round_score_submission.html", {'submission_form': submission_form, 'score_form': score_form, 'teetime_data': teetime_data})









# def load_tees(request):
#     print(request.GET)
#     course_id = request.GET.get('course')
#     tees = Golf_Tee.objects.filter(course_id=course_id)
#     return render(request, 'round_dropdown_list_options.html', {'tees': tees})
