from django import forms
from GolfRound.models import Round_Score, Net_Round_Score
from golf_trip.models import Trip_TeeTime
from django.forms import modelformset_factory



class RoundScoreForm(forms.ModelForm):
    round_golfer = forms.CharField(widget=forms.TextInput(attrs={'style': 'width:75px; background-color: 	#D3D3D3', 'padding-right':'100px', 'readonly': 'readonly'}))
    total_score = forms.IntegerField(required=False)
    net_score = forms.IntegerField(required=False)

    class Meta():
        fields = '__all__'
        model = Round_Score

        widgets = {
            #score section of form
            'golfer_index': forms.TextInput(attrs={'class': 'td-score', 'style': 'background-color: #D3D3D3', 'padding-right':'100px', 'readonly': 'readonly'}),
            'hole_1_score': forms.TextInput(attrs={'class': 'td-score'}),
            'hole_2_score': forms.TextInput(attrs={'class': 'td-score'}),
            'hole_3_score': forms.TextInput(attrs={'class': 'td-score'}),
            'hole_4_score': forms.TextInput(attrs={'class': 'td-score'}),
            'hole_5_score': forms.TextInput(attrs={'class': 'td-score'}),
            'hole_6_score': forms.TextInput(attrs={'class': 'td-score'}),
            'hole_7_score': forms.TextInput(attrs={'class': 'td-score'}),
            'hole_8_score': forms.TextInput(attrs={'class': 'td-score'}),
            'hole_9_score': forms.TextInput(attrs={'class': 'td-score'}),
            'hole_10_score': forms.TextInput(attrs={'class': 'td-score'}),
            'hole_11_score': forms.TextInput(attrs={'class': 'td-score'}),
            'hole_12_score': forms.TextInput(attrs={'class': 'td-score'}),
            'hole_13_score': forms.TextInput(attrs={'class': 'td-score'}),
            'hole_14_score': forms.TextInput(attrs={'class': 'td-score'}),
            'hole_15_score': forms.TextInput(attrs={'class': 'td-score'}),
            'hole_16_score': forms.TextInput(attrs={'class': 'td-score'}),
            'hole_17_score': forms.TextInput(attrs={'class': 'td-score'}),
            'hole_18_score': forms.TextInput(attrs={'class': 'td-score'}),
            'total_score': forms.TextInput(attrs={'class': 'td-score'}),
            'net_score': forms.TextInput(attrs={'class': 'td-score'}),
        }


scoreform = modelformset_factory(Round_Score, fields=('__all__'), form=RoundScoreForm, extra=4,  max_num=5)

