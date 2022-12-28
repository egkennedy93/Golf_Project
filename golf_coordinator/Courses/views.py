
from django.shortcuts import render, get_object_or_404, redirect
from Courses.models import Golf_Course, Golf_Tee
from Courses.forms import AddCourseForm, AddTeeForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView, ListView, DetailView, UpdateView, CreateView, DeleteView)
from django.utils.timezone import now
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.forms import inlineformset_factory
# Create your views here.



def CreateCourseView(request):

    TeeFormSet = inlineformset_factory(Golf_Course, Golf_Tee, form=AddTeeForm, fields=('__all__', ), extra=1,)
    if request.method == "POST":
        
        course_form = AddCourseForm(request.POST)
        teeformset = TeeFormSet(request.POST, instance=course_form.instance)        
            # Do something. Should generally end with a redirect. For example:
        if course_form.is_valid():
            course_form.save()           
        
        if teeformset.is_valid():
             teeformset.save()

        return redirect("/")
    else:
        course_form = AddCourseForm()
        teeformset = TeeFormSet
    return render(request, "Courses/add_course_form.html", {'teeformset': teeformset,'course_form': course_form, })
