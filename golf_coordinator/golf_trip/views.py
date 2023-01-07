from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from golf_trip.models import Trip_Golfer

class HomePage(TemplateView):
    template_name = 'golf_trip/trip_2023_index.html'
    extra_context={'golfers': Trip_Golfer.objects.all()}