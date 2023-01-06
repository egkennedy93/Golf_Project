from django import forms
from GolfRound.models import Golf_Round, Round_Submission
from Courses.models import Golf_Course, Golf_Tee
from django.forms import formset_factory


class CreateGolfRoundForm(forms.ModelForm):
    course = forms.ModelChoiceField(queryset=Golf_Course.objects.all().values_list('course_name', flat=True))
    class Meta:
        model = Golf_Round
        exclude = ['is_active_round', 'round_create_date',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tee'].queryset = Golf_Tee.objects.none()


class RoundSubmissionForm(forms.ModelForm):
    course = forms.ModelChoiceField(queryset=Golf_Course.objects.all().values_list('course_name', flat=True))
    class Meta:
        model = Round_Submission
        exclude = ['round_submission_date',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tee'].queryset = Golf_Tee.objects.none()

