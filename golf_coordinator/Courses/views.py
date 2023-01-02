
from django.shortcuts import render, redirect
from Courses.models import Golf_Course, Golf_Tee
from Courses.forms import AddCourseForm, AddTeeForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView, ListView, DetailView, UpdateView, CreateView, DeleteView)
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.forms import inlineformset_factory
# Create your views here.



def CreateCourseView(request):

    TeeFormSet = inlineformset_factory(Golf_Course, Golf_Tee, form=AddTeeForm, extra=1,)
    if request.method == "POST":
        course_form = AddCourseForm(request.POST)
        teeformset = TeeFormSet(request.POST, instance=course_form.instance)
        cleaned_tee = []
           
        if course_form.is_valid():
            course_form.save()           
        
        if teeformset.is_valid():
            teeformset.save()

        return render(request,'Courses/course_submission.html',{'course_data': course_form.cleaned_data})
    else:
        course_form = AddCourseForm()
        teeformset = TeeFormSet()
    return render(request, "Courses/add_course_form.html", {'teeformset': teeformset,'course_form': course_form,})



class Golf_CourseListView(ListView):
    model = Golf_Course

class Golf_CourseDetailView(DetailView):
    model = Golf_Course
    context_object_name = 'golf_course'

class Golf_TeeDetailView(DetailView):
    model = Golf_Tee
    context_object_name = 'golf_tee'

class Golf_TeeCreateView(CreateView):
    model = Golf_Tee
    fields = ('__all__')
    context_object_name = 'golf_tee'






