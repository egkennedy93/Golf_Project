from django import forms
from Courses.models import Golf_Course, Golf_Tee, Golf_Hole


class AddCourseForm(forms.ModelForm):

    class Meta():
        fields = ('course_name',)
        model = Golf_Course
        

class AddTeeForm(forms.ModelForm):
    class Meta():
        fields = ('course_name', 'tee_name', 'par', 'slope', 'rating', 'yardage')
        widgets = {
            'rating': forms.NumberInput(attrs={'step': 0.25}),
        }
        model = Golf_Tee


class AddHoleForm(forms.ModelForm):
    class Meta():
        fields = ('course_name', 'referred_tee_name', 'hole_number', 'par', 'yardage', 'hcp_index')
        model = Golf_Hole
