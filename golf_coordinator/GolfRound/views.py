from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DetailView
from Courses.models import Golf_Tee
from django.urls import reverse_lazy
from django.forms import inlineformset_factory
from GolfRound.forms import RoundSubmissionForm, RoundScoreForm
from GolfRound.models import Round_Submission



def RoundSubmissionView(request):
    # inlineformet is being used to update the Golf_Tee and Golf_Course under the same form POST 
    # TeeFormSet = inlineformset_factory(Golf_Course, Golf_Tee, form=AddTeeForm, extra=1,)
    if request.method == "POST":
        submission_form = RoundSubmissionForm(request.POST)
        # teeformset = TeeFormSet(request.POST, instance=course_form.instance)
        
        # validating and saving the course_form data
        if submission_form.is_valid():
            submission_form.save()           
        
        # validating and saving the GolfTee_form data
        # if teeformset.is_valid():
        #     teeformset.save()

        # the dictionary paseed is what gets rendered for the html template. Whatever is listed there can be access on the template
        return render(request,'Courses/course_submission.html',{'course_data': course_form.cleaned_data})
    else:
        course_form = RoundSubmissionForm()
        # teeformset = TeeFormSet()
    return render(request, "round/submission.html", {'submission_form': submission_form,})









# def load_tees(request):
#     print(request.GET)
#     course_id = request.GET.get('course')
#     tees = Golf_Tee.objects.filter(course_id=course_id)
#     return render(request, 'round_dropdown_list_options.html', {'tees': tees})
