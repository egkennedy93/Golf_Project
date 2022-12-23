from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from Courses.models import Golf_Course, Golf_Tee, Golf_Hole
from Courses.forms import AddCourseForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView, ListView, DetailView, UpdateView, CreateView, DeleteView)
from django.utils.timezone import now
from django.contrib.auth.decorators import login_required

# Create your views here.



class CreateCourseView(CreateView):
    login_url = '/login/'
    form_class = AddCourseForm
    redirect_field_name = 'about.html'
    model = Golf_Course
