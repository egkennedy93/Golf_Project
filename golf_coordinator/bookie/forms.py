from django import forms
from bookie.models import * 
from golf_trip.models import Trip_TeeTime
from django.forms import modelformset_factory


class BetTeeTimeForm(forms.ModelForm):
    CHOICES = [
        ('1', 'Bet against Player'),
        ('2', 'Bet against Team'),
    ]

    bet_type = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES, required=False, initial='1')

    class Meta():
        fields = ['submitter', 'opponent', 'units', 'bet_tee_time']
        model = TeeTimeBet
