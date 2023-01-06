from django import forms
from GolfRound.models import Round_Submission
from Courses.models import Golf_Course, Golf_Tee
from django.forms import formset_factory


class RoundSubmissionForm(forms.ModelForm):
    class Meta:
        model = Round_Submission
        exclude = ['round_submission_date',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tee'].queryset = Golf_Tee.objects.none()

        if 'course' in self.data:
            try:
                course_id = int(self.data.get('course'))
                self.fields['tee'].queryset = Golf_Tee.objects.filter(course_id=course_id)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['tee'].queryset = self.instance.golf_course.tee_set.order_by('name')

