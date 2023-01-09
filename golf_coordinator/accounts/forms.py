from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Golfer
from django import forms
from django.contrib.auth.models import User


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
