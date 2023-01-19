from django import forms
from GolfRound.models import Round_Submission, Round_Score
from django.forms import formset_factory


class RoundSubmissionForm(forms.ModelForm):

    class Meta():
        fields = '__all__'
        model = Round_Submission


class RoundScoreForm(forms.ModelForm):

    class Meta():
        fields = '__all__'
        model = Round_Score

        widgets = {
            #score section of form
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
        }













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

