from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from accounts.forms import GolferInfoForm, UserForm

from . import forms
# Create your views here.

# inherits the generic createview so users can sign up.

class SignUp(CreateView):
    form_class = forms.GolferInfoForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

'''
This is functionality is not being used. Currently not suporting other users to have their own accounts. Will look to add in a 
future release
'''

def register(request):
    registered = False

    if request.method == "POST":
        # instaniates the user and golfer views
        user_form = UserForm(data=request.POST)
        golfer_form = GolferInfoForm(data=request.POST)

        if user_form.is_valid() and golfer_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            golfer = golfer_form.save(commit=False)
            golfer.user = user

            if  'profile_pic' in request.FILES:
                golfer.picture = request.FILES['picture']
            
            golfer.save()

            registered = True
        else:
            print(user_form.errors, golfer_form.errors)
    else:
        user_form = UserForm()
        golfer_form = GolferInfoForm()
    # returns the user_form, golfer_form and registered data into the context to be used in the html templates
    return render(request, 'accounts/signup.html', {'user_form':user_form,
                                                   'golfer_form': golfer_form,
                                                   'registered': registered})
