from django import forms
from Courses.models import Golf_Course, Golf_Tee, Golf_Hole


class AddCourseForm(forms.ModelForm):

    class Meta():
        fields = ('name',)
        model = Golf_Course
        

class AddTeeForm(forms.ModelForm):
    class Meta():
        fields = ('course', 'tee_name', 'tee_color', 'par', 'slope', 'rating', 'yardage')
        model = Golf_Tee


class AddHoleForm(forms.ModelForm):
    class Meta():
        fields = ('course', 'tee', 'hole_number', 'par', 'yardage', 'hcp_index')
        model = Golf_Hole
