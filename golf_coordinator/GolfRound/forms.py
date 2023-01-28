from django import forms
from GolfRound.models import Round_Score
from golf_trip.models import Trip_TeeTime
from django.forms import modelformset_factory



class RoundScoreForm(forms.ModelForm):
    round_golfer = forms.CharField(disabled=True, widget=forms.TextInput(attrs={'style': 'width:75px', 'padding-right':'100px'}))

    class Meta():
        fields = '__all__'
        model = Round_Score

        widgets = {
            #score section of form
            'golfer_index': forms.TextInput(attrs={'class': 'td-score'}),
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












# class RoundSubmissionForm(forms.ModelForm):
#     class Meta:
#         model = Round_Submission
#         exclude = ['round_submission_date',]

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['tee'].queryset = Golf_Tee.objects.none()

#         if 'course' in self.data:
#             try:
#                 course_id = int(self.data.get('course'))
#                 self.fields['tee'].queryset = Golf_Tee.objects.filter(course_id=course_id)
#             except (ValueError, TypeError):
#                 pass  # invalid input from the client; ignore and fallback to empty City queryset
#         elif self.instance.pk:
#             self.fields['tee'].queryset = self.instance.golf_course.tee_set.order_by('name')

