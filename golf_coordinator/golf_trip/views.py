from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, DetailView, ListView
from golf_trip.models import Trip_Golfer, Trip_Event, Golf_Trip, Trip_Course


class EventHistoryView(ListView):
    model = Golf_Trip


class HistoryStreamsong(TemplateView):
    template_name = 'golf_trip/trip_streamsong_index.html'
    extra_context={'golfers': Trip_Golfer.objects.all().filter(trip__trip_name='Streamsong'), 
                   'trip_events':Trip_Event.objects.all().filter(trip__trip_name='Streamsong')}


class HomePage(TemplateView):
    template_name = 'golf_trip/trip_michigan_index.html'
    extra_context={'golfers': Trip_Golfer.objects.all().filter(trip__trip_name='Michigan'), 
                   'trip_events':Trip_Event.objects.all().filter(trip__trip_name='Michigan')}


class EventDetailView(DetailView):
    model = Trip_Event
    template_name='golf_trip/golf_trip_detail.html'


class PlayersListView(ListView):
    model = Trip_Golfer

    def get_queryset(self):
        queryset = Trip_Golfer.objects.all().filter(trip__trip_name='Michigan').order_by('golfer__first_name')
        
        return queryset


class EventListView(ListView):
    model = Trip_Event

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(EventListView, self).get_context_data(**kwargs)
        # Add in the publisher
        trip_dates = Trip_Event.objects.all().filter(trip__trip_name='Michigan').values('event_time').distinct()
        trip_courses = Trip_Event.objects.all().filter(trip__trip_name='Michigan')

        context['trip_events'] = trip_courses
        context['trip_dates'] = trip_dates
        return context


class EventDayListView(ListView):
    model = Trip_Event
    