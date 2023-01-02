from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Golfer
from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
   

    class Meta():
        model = User
        fields = '__all__'

class GolferInfoForm(forms.ModelForm):

    class Meta():
        model = Golfer
        fields = ('portfolio', 'picture', 'hcp_index')

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['username'].label = 'Display Name'
    #     self.fields['email'].label = "Email Address"