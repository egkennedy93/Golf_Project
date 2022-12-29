from django import forms
from Courses.models import Golf_Course, Golf_Tee
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
            'rating': forms.NumberInput(attrs={'step': 1}),
            'hole_1_yardage': forms.TextInput(attrs={'size': 1}),
            'hole_2_yardage': forms.TextInput(attrs={'size': 1}),
            'hole_3_yardage': forms.TextInput(attrs={'size': 1}),
            'hole_4_yardage': forms.TextInput(attrs={'size': 1}),
            'hole_5_yardage': forms.TextInput(attrs={'size': 1}),
            'hole_6_yardage': forms.TextInput(attrs={'size': 1}),
            'hole_7_yardage': forms.TextInput(attrs={'size': 1}),
            'hole_8_yardage': forms.TextInput(attrs={'size': 1}),
            'hole_9_yardage': forms.TextInput(attrs={'size': 1}),
            'hole_10_yardage': forms.TextInput(attrs={'size': 1}),
            'hole_11_yardage': forms.TextInput(attrs={'size': 1}),
            'hole_12_yardage': forms.TextInput(attrs={'size': 1}),
            'hole_13_yardage': forms.TextInput(attrs={'size': 1}),
            'hole_14_yardage': forms.TextInput(attrs={'size': 1}),
            'hole_15_yardage': forms.TextInput(attrs={'size': 1}),
            'hole_16_yardage': forms.TextInput(attrs={'size': 1}),
            'hole_17_yardage': forms.TextInput(attrs={'size': 1}),
            'hole_18_yardage': forms.TextInput(attrs={'size': 1}),

            'hole_1_par': forms.Select(attrs={'style': 'width:50px'}),
            'hole_2_par': forms.Select(attrs={'style': 'width:50px'}),
            'hole_3_par': forms.Select(attrs={'style': 'width:50px'}),
            'hole_4_par': forms.Select(attrs={'style': 'width:50px'}),
            'hole_5_par': forms.Select(attrs={'style': 'width:50px'}),
            'hole_6_par': forms.Select(attrs={'style': 'width:50px'}),
            'hole_7_par': forms.Select(attrs={'style': 'width:50px'}),
            'hole_8_par': forms.Select(attrs={'style': 'width:50px'}),
            'hole_9_par': forms.Select(attrs={'style': 'width:50px'}),
            'hole_10_par': forms.Select(attrs={'style': 'width:50px'}),
            'hole_11_par': forms.Select(attrs={'style': 'width:50px'}),
            'hole_12_par': forms.Select(attrs={'style': 'width:50px'}),
            'hole_13_par': forms.Select(attrs={'style': 'width:50px'}),
            'hole_14_par': forms.Select(attrs={'style': 'width:50px'}),
            'hole_15_par': forms.Select(attrs={'style': 'width:50px'}),
            'hole_16_par': forms.Select(attrs={'style': 'width:50px'}),
            'hole_17_par': forms.Select(attrs={'style': 'width:50px'}),
            'hole_18_par': forms.Select(attrs={'style': 'width:50px'}),

            'hole_1_index': forms.Select(attrs={'style': 'width:50px'}),
            'hole_2_index': forms.Select(attrs={'style': 'width:50px'}),
            'hole_3_index': forms.Select(attrs={'style': 'width:50px'}),
            'hole_4_index': forms.Select(attrs={'style': 'width:50px'}),
            'hole_5_index': forms.Select(attrs={'style': 'width:50px'}),
            'hole_6_index': forms.Select(attrs={'style': 'width:50px'}),
            'hole_7_index': forms.Select(attrs={'style': 'width:50px'}),
            'hole_8_index': forms.Select(attrs={'style': 'width:50px'}),
            'hole_9_index': forms.Select(attrs={'style': 'width:50px'}),
            'hole_10_index': forms.Select(attrs={'style': 'width:50px'}),
            'hole_11_index': forms.Select(attrs={'style': 'width:50px'}),
            'hole_12_index': forms.Select(attrs={'style': 'width:50px'}),
            'hole_13_index': forms.Select(attrs={'style': 'width:50px'}),
            'hole_14_index': forms.Select(attrs={'style': 'width:50px'}),
            'hole_15_index': forms.Select(attrs={'style': 'width:50px'}),
            'hole_16_index': forms.Select(attrs={'style': 'width:50px'}),
            'hole_17_index': forms.Select(attrs={'style': 'width:50px'}),
            'hole_18_index': forms.Select(attrs={'style': 'width:50px'}),   
        }
        model = Golf_Tee

