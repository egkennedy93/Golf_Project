from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Golfer
from django import forms
from django.contrib.auth.models import User

'''
These forms currently exist, but they are not being used. The app doesn't handle users to be using the app, but for a admin to be running
the trip. Future features are planned so users cna create and manage their own trips. 
'''

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
   

    class Meta():
        model = User
        fields = ('username', 'password','first_name', 'last_name', 'email')


class GolferInfoForm(forms.ModelForm):

    class Meta():
        model = Golfer
        fields = ('first_name', 'last_name')
        picture = forms.ImageField(required=False)
