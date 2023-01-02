
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
    # inlineformet is being used to update the Golf_Tee and Golf_Course under the same form POST 
    TeeFormSet = inlineformset_factory(Golf_Course, Golf_Tee, form=AddTeeForm, extra=1,)
    if request.method == "POST":
        course_form = AddCourseForm(request.POST)
        teeformset = TeeFormSet(request.POST, instance=course_form.instance)
        
        # validating and saving the course_form data
        if course_form.is_valid():
            course_form.save()           
        
        # validating and saving the GolfTee_form data
        if teeformset.is_valid():
            teeformset.save()

        # the dictionary paseed is what gets rendered for the html template. Whatever is listed there can be access on the template
        return render(request,'Courses/course_submission.html',{'course_data': course_form.cleaned_data})
    else:
        course_form = AddCourseForm()
        teeformset = TeeFormSet()
    return render(request, "Courses/add_course_form.html", {'teeformset': teeformset,'course_form': course_form,})


# view that shows a list of courses
class Golf_CourseListView(ListView):
    model = Golf_Course

#view that shows all of the avilable tees for a golfcourse
class Golf_CourseDetailView(DetailView):
    model = Golf_Course
    context_object_name = 'golf_course'

# selecting a tee and showing the "scorecard" for that tee
class Golf_TeeDetailView(DetailView):
    model = Golf_Tee
    context_object_name = 'golf_tee'

# create view to add another tee to a course
class Golf_TeeCreateView(CreateView):
    model = Golf_Tee
    fields = ('__all__')
    context_object_name = 'golf_tee'






