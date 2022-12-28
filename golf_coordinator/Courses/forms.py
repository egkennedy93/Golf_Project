from django import forms
from Courses.models import Golf_Course, Golf_Tee, Golf_Hole
from django.forms import inlineformset_factory


class AddCourseForm(forms.ModelForm):

    class Meta():
        fields = '__all__'
        model = Golf_Course
        

class AddTeeForm(forms.ModelForm):
    class Meta():
        # exclude = ('course_name',)
        fields = '__all__'
        widgets = {
            'rating': forms.NumberInput(attrs={'step': 0.1}),
        }
        model = Golf_Tee


class AddHoleForm(forms.ModelForm):
    class Meta():
        # fields = ('hole_number', 'par', 'yardage', 'hcp_index',)
        fields = '__all__'
        model = Golf_Hole

