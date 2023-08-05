from django import forms
from GolfRound.models import Round_Score, Net_Round_Score, Par3_Round_Score, Par3_Net_Round_Score
from golf_trip.models import Trip_TeeTime, Trip_Golfer
from django.forms import modelformset_factory



class RoundScoreForm(forms.ModelForm):
    round_golfer = forms.CharField(widget=forms.TextInput(attrs={'class': 'td-player', 'style': 'width: 150px; background-color: 	#D3D3D3', 'padding-right':'100px', 'readonly': 'readonly'}))
    total_score = forms.IntegerField(required=False)
    net_score = forms.IntegerField(required=False)

    class Meta():
        fields = '__all__'
        model = Round_Score


        widgets = {
            #score section of form
            'golfer_pk': forms.HiddenInput(),
            'golfer_index': forms.TextInput(attrs={'class': 'td-player', 'style': 'width: 60px; background-color: #D3D3D3', 'padding-right':'300px', 'readonly': 'readonly'}),
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
            'round_golfer': forms.TextInput(attrs={'class': 'td-score'}),
            'scramble_HCP': forms.TextInput(attrs={'class': 'td-score'}),
        }
    


scoreform = modelformset_factory(Round_Score, fields=('__all__'), form=RoundScoreForm, extra=4,  max_num=5)
scoreform_1v1 = modelformset_factory(Round_Score, fields=('__all__'), form=RoundScoreForm, extra=2,  max_num=5)

class Par3RoundScoreForm(forms.ModelForm):
    round_golfer = forms.CharField(widget=forms.TextInput(attrs={'class': 'td-player', 'style': 'width: 150px; background-color: 	#D3D3D3', 'padding-right':'100px', 'readonly': 'readonly'}))
    total_score = forms.IntegerField(required=False)
    net_score = forms.IntegerField(required=False)

    class Meta():
        fields = '__all__'
        model = Round_Score


        widgets = {
            #score section of form
            'golfer_pk': forms.HiddenInput(),
            'golfer_index': forms.TextInput(attrs={'class': 'td-player', 'style': 'width: 60px; background-color: #D3D3D3', 'padding-right':'300px', 'readonly': 'readonly'}),
            'hole_1_score': forms.TextInput(attrs={'class': 'td-score'}),
            'hole_2_score': forms.TextInput(attrs={'class': 'td-score'}),
            'hole_3_score': forms.TextInput(attrs={'class': 'td-score'}),
            'hole_4_score': forms.TextInput(attrs={'class': 'td-score'}),
            'hole_5_score': forms.TextInput(attrs={'class': 'td-score'}),
            'hole_6_score': forms.TextInput(attrs={'class': 'td-score'}),
            'hole_7_score': forms.TextInput(attrs={'class': 'td-score'}),
            'hole_8_score': forms.TextInput(attrs={'class': 'td-score'}),
            'hole_9_score': forms.TextInput(attrs={'class': 'td-score'}),
            'total_score': forms.TextInput(attrs={'class': 'td-score'}),
            'net_score': forms.TextInput(attrs={'class': 'td-score'}),
            'round_golfer': forms.TextInput(attrs={'class': 'td-score'}),
            'scramble_HCP': forms.TextInput(attrs={'class': 'td-score'}),
        }

par3scoreform = modelformset_factory(Par3_Round_Score, fields=('__all__'), form=Par3RoundScoreForm, extra=4,  max_num=5)

