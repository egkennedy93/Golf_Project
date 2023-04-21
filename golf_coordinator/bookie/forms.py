from django import forms
from bookie.models import * 
from golf_trip.models import Trip_TeeTime, Trip_Golfer
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
        widgets = {'bet_tee_time': forms.HiddenInput()}

    def __init__(self, teetime_pk, **kwargs):
        super(BetTeeTimeForm, self).__init__(**kwargs)
        if teetime_pk:
            pass
            self.fields['opponent'].queryset = Trip_TeeTime.objects.filter(pk=teetime_pk).values_list('Players__golfer__last_name', flat=True)
            self.fields['bet_tee_time'].queryset = Trip_TeeTime.objects.filter(pk=teetime_pk)
