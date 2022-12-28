
from django.shortcuts import render, get_object_or_404, redirect
from Courses.models import Golf_Course, Golf_Tee, Golf_Hole
from Courses.forms import AddCourseForm, AddTeeForm, AddHoleForm
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

    TeeFormSet = inlineformset_factory(Golf_Course, Golf_Tee, form=AddTeeForm, fields=('tee_name', 'course_par', 'slope', 'rating', 'yardage',), extra=1,)
    HoleFormSet = inlineformset_factory(Golf_Tee, Golf_Hole, form=AddHoleForm, fields=('hole_number', 'par', 'yardage', 'hcp_index',), extra=18, )
    if request.method == "POST":
        
        course_form = AddCourseForm(request.POST)
        teeformset = TeeFormSet(request.POST, instance=course_form.instance)
        holeformset = HoleFormSet(request.POST, instance=teeformset.instance)
        
            # Do something. Should generally end with a redirect. For example:
        if course_form.is_valid():
            course_form.save()           
        
        if holeformset.is_valid():
            holeformset.save()
        
        if teeformset.is_valid():
             teeformset.save()

        return redirect("/")
    else:
        course_form = AddCourseForm()
        teeformset = TeeFormSet
        holeformset = HoleFormSet
    return render(request, "Courses/add_course_form.html", {'teeformset': teeformset,'course_form': course_form, 'holeformset': holeformset,})

# def CreateCourseView(request):
#     context = {}
#     formset = HoleFormSet(request.POST)
        
#     if request.method == "POST":
#         course_form = AddCourseForm(request.POST)

#         if formset.is_valid():
#             formset.save()
#         context['formset']

        
#         if course_form.is_valid():
#             course_form.save()

#         if tee_form.is_valid():
#             tee_form.save()

#         if hole_form.is_valid():
#             hole_form.save()

#             messages.success(request, ('Your course was successfully added!'))
#         else:
#             messages.error(request, 'Error saving form')
#         return redirect("courses/")
#     course_form = AddCourseForm()
#     tee_form = AddTeeForm()
#     hole_form = AddHoleForm()
#     courses = Golf_Course.objects.all()
#     tees = Golf_Tee.objects.all()
#     holes=Golf_Hole.objects.all()
#     context.update({'course_form':course_form, 'courses':courses, 'tee_form': tee_form, 'tees': tees, 'hole_form': hole_form, 'holes': holes})
        
#     return render(request=request, template_name="Courses/add_course_form.html", context=context)

