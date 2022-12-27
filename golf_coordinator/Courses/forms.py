from django import forms
from Courses.models import Golf_Course, Golf_Tee, Golf_Hole


class AddCourseForm(forms.ModelForm):

    class Meta():
        fields = ('__all__')
        model = Golf_Course
        

class AddTeeForm(forms.ModelForm):
    class Meta():
        exclude = ('course_name', 'referred_tee_name',)
        widgets = {
            'rating': forms.NumberInput(attrs={'step': 0.25}),
        }
        model = Golf_Tee


class AddHoleForm(forms.ModelForm):
    class Meta():
        fields = ('hole_number', 'par', 'yardage', 'hcp_index',)
        model = Golf_Hole

HoleFormSet = forms.formset_factory(AddHoleForm, extra=17)
