from django import forms
from GolfRound.models import Golf_Round, Round_Hole_Player
from django.forms import formset_factory




class CreateGolfRoundForm(forms.ModelForm):
    class Meta:
        model = Golf_Round
        fields = ['tee', 'course']

class CreateGolfRoundScoreForm(forms.ModelForm):
    class Meta:
        model = Round_Hole_Player
        fields = '__all__'
        
