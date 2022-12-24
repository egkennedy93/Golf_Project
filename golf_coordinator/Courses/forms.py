from django import forms
from Courses.models import Golf_Course, Golf_Tee, Golf_Hole


class AddCourseForm(forms.ModelForm):

    class Meta():
        model = Golf_Course
        fields = ('name',)
        

class AddCourseTeeForm(forms.ModelForm):
    class Meta():
        model = Golf_Tee
        fields = ('tee_color', 'tee_name', 'par', 'slope', 'rating', 'yardage',)

class AddCourseHoleForm(forms.ModelForm):
    class Meta():
        model = Golf_Hole
