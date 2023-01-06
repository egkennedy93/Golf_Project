from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DetailView
from Courses.models import Golf_Tee
from django.urls import reverse_lazy
from django.forms import inlineformset_factory
from GolfRound.forms import RoundSubmissionForm
from GolfRound.models import Round_Submission



class CreateRoundSubmissionView(CreateView):
    form_class = RoundSubmissionForm
    model = Round_Submission
    redirect_field_name = 'golfround/round_submit.html'

class RoundDetailView(DetailView):
    model = Round_Submission
    


def load_tees(request):
    print(request.GET)
    course_id = request.GET.get('course')
    tees = Golf_Tee.objects.filter(course_id=course_id)
    return render(request, 'round_dropdown_list_options.html', {'tees': tees})
