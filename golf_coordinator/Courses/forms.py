from django import forms
from Courses.models import Golf_Course, Golf_Tee, Golf_Hole


class AddCourseForm(forms.ModelForm):

    class Meta():
        model = Golf_Course
        fields = ('name',)
        widgets = {
            'Name': forms.TextInput(attrs={'class': 'textinputclass'}),
        }

class AddCourseTeeForm(forms.ModelForm):
    class Meta():
        model = Golf_Tee
        fields = ('tee_color', 'tee_name', 'par', 'slope', 'rating', 'yardage',)