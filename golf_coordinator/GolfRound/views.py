from django.shortcuts import render
from django.views.generic import CreateView
from GolfRound.models import Golf_Round
from Courses.models import Golf_Tee
from django.urls import reverse_lazy
from django.forms import inlineformset_factory
from GolfRound.forms import CreateGolfRoundForm
 

# Create your views here.
def CreateRoundView(request):
    # inlineformet is being used to update the Golf_Tee and Golf_Course under the same form POST 
    # roundholescore_formset = inlineformset_factory(Golf_Round, Round_Hole_Player, form=CreateGolfRoundScoreForm, extra=4,)
    if request.method == "POST":
        round_form = CreateGolfRoundForm(request.POST)
        
        # validating and saving the course_form data

        if round_form.is_valid():
            round_form.save()           
       

        # the dictionary paseed is what gets rendered for the html template. Whatever is listed there can be access on the template
        return render(request,'Courses/course_submission.html',{'round_form': round_form.cleaned_data})
    else:

        round_form = CreateGolfRoundForm()
        tee_data = Golf_Tee.objects.all()

    return render(request, "GolfRound/golfround_form.html", {'round_form': round_form, 'tee_data': tee_data})


def load_tees(request):
    course_id = request.GET.get('course')
    tees = Golf_Tee.objects.filter(course_id=1)
    return render(request, 'round_dropdown_list_options.html', {'tees': tees})
