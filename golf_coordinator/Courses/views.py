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
# Create your views here.



def CreateCourseView(request):
    if request.method == "POST":
        courseform = AddCourseForm(request.POST, instance=Golf_Course())
        teeform = AddTeeForm(request.POST, instance=Golf_Tee())
        holeforms = [AddHoleForm(request.POST, instance=Golf_Hole()) for x in range(0,3)]
        if courseform.is_valid() and teeform.is_valid() and all([hole.is_valid() for hole in holeforms]):
            courseform.save()
            teeform.save()
            holeform.save()
            return HttpResponseRedirect('/Courses/')
    else:
        courseform = AddCourseForm(instance=Golf_Course())
        teeform = AddCourseForm(instance=Golf_Tee())
        holeform = AddHoleForm(instance=Golf_Hole)
    return render(request, 'Courses/add_course_form.html', {'Golf_Course_form': courseform, 'Golf_Tee_form': teeform, 'Golf_Hole_form': holeform})
