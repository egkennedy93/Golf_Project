from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, DetailView, ListView
from golf_trip.models import Trip_Golfer, Trip_Event, Golf_Trip


class EventHistoryView(ListView):
    model = Golf_Trip


class HistoryStreamsong(TemplateView):
    template_name = 'golf_trip/trip_streamsong_index.html'
    extra_context={'golfers': Trip_Golfer.objects.all().filter(trip__trip_name='Streamsong'), 
                   'trip_events':Trip_Event.objects.all().filter(trip__trip_name='Streamsong')}


class HomePage(TemplateView):
    template_name = 'golf_trip/trip_2023_index.html'
    extra_context={'golfers': Trip_Golfer.objects.all().filter(trip__trip_name='Michigan'), 
                   'trip_events':Trip_Event.objects.all().filter(trip__trip_name='Michigan')}


class EventDetailView(DetailView):
    model = Trip_Event
    template_name='golf_trip/golf_trip_detail.html'





# class HomePage(TemplateView):
#     template_name = 'golf_trip/trip_2022_index.html'
    # try:
    #     golfers = Trip_Golfer.objects.all.filter
    # extra_context={'golfers': Trip_Golfer.objects.all()., 'trip_events':Trip_Event.objects.all()}