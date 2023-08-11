from django import forms
from bookie.models import * 
from golf_trip.models import Trip_TeeTime, Trip_Golfer
from django.forms import modelformset_factory


class BetTeeTimeForm(forms.ModelForm):
    CHOICES = [
        ('1', 'Bet against Player'),
    ]


    class Meta():
        fields = ['submitter', 'opponent', 'units', 'bet_tee_time', 'bet_type']
        model = GolfBet
        widgets = { 
                   'bet_tee_time': forms.HiddenInput(),
                   'units': forms.TextInput(attrs={'class': 'form-control input-group', 'style': "max-width:5em; margin:auto;", 'placeholder': '5.00'}),
                   'submitter': forms.Select(attrs={'style': "max-width:10em; margin:auto;", 'class': 'form-select'}),
                   'opponent': forms.Select(attrs={'style': "max-width:10em; margin:auto", 'class': 'form-select'}),
                   'bet_type': forms.RadioSelect(attrs={'style': "max-width:10em"}),
                   }
        

    def __init__(self, *args, **kwargs):
        teetime_pk = kwargs.pop('teetime_pk')
        super(BetTeeTimeForm, self).__init__(*args, **kwargs)
        if teetime_pk:
            self.fields['bet_tee_time'].queryset = Trip_TeeTime.objects.filter(pk=teetime_pk)
