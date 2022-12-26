from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from Courses.models import Golf_Course, Golf_Tee, Golf_Hole
from Courses.forms import AddCourseForm, AddTeeForm, AddHoleForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView, ListView, DetailView, UpdateView, CreateView, DeleteView)
from django.utils.timezone import now
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from . import forms
# Create your views here.


def CreateCourseView(request):

    if request.method == "POST":
        course_form = AddCourseForm(request.POST)
        tee_form = AddTeeForm(request.POST)
        if course_form.is_valid():
            course_form.save()
            tee_form.is_valid()
            tee_form.save()
            messages.success(request, ('Your course was successfully added!'))
        else:
            messages.error(request, 'Error saving form')
        return redirect("courses/")
    course_form = AddCourseForm()
    tee_form = AddTeeForm()
    courses = Golf_Course.objects.all()
    tees = Golf_Tee.objects.all()
    return render(request=request, template_name="Courses/add_course_form.html", context={'course_form':course_form, 'movies':courses, 'tee_form': tee_form, 'tees': tees})



# def CreateCourseView(request):
#     if request.method == "POST":
#         courseform = AddCourseForm(request.POST, prefix='course')
#         teeform = AddTeeForm(request.POST, prefix='tee')
#         holeform = AddHoleForm(request.POST, prefix='hole')
#         if courseform.is_valid() and teeform.is_valid() and holeform.is_valid():
#             course_name = courseform.cleaned_data['course_name']
#             course_tee = teeform.cleaned_data['tee_name']



#             course = courseform.save()
#             tee = teeform.save()
#         return render(request, 'Courses/add_course_form.html')
#     else:
#         courseform = AddCourseForm(prefix='course')
#         teeform = AddTeeForm(prefix='tee')
#         holeform = AddHoleForm(prefix='hole')
#         # args = {'courseform': courseform, 'teeform': teeform, 'holeform': holeform}
#         courses = Golf_Course.objects.all()
#     return render(request, 'Courses/add_course_form.html', context={"coursform": courseform, "courses": courses })
