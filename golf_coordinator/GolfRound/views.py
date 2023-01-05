from django.shortcuts import render
from django.views.generic import CreateView
from GolfRound.models import Golf_Round, Round_Hole_Player
from django.urls import reverse_lazy
from django.forms import inlineformset_factory
from GolfRound.forms import CreateGolfRoundScoreForm, CreateGolfRoundForm
 

# Create your views here.
def CreateRoundView(request):
    # inlineformet is being used to update the Golf_Tee and Golf_Course under the same form POST 
    roundholescore_formset = inlineformset_factory(Golf_Round, Round_Hole_Player, form=CreateGolfRoundScoreForm, extra=4,)
    if request.method == "POST":
        round_form = CreateGolfRoundForm(request.POST)
        roundholescore_formset = CreateGolfRoundScoreForm(request.POST, instance=round_form.instance)
        
        # validating and saving the course_form data
        if round_form.is_valid():
            round_form.save()           
        
        # validating and saving the GolfTee_form data
        if roundholescore_formset.is_valid():
            roundholescore_formset.save()

        # the dictionary paseed is what gets rendered for the html template. Whatever is listed there can be access on the template
        return render(request,'Courses/course_submission.html',{'round_form': round_form.cleaned_data})
    else:
        round_form = CreateGolfRoundForm()
        roundholescore_formset = CreateGolfRoundScoreForm()
        round_data = Golf_Round.objects.all()
    return render(request, "GolfRound/golfround_form.html", {'round_form': round_form, 'roundholescore_formset': roundholescore_formset, 'round_data': round_data})
