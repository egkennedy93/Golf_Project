from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, DetailView, ListView
from golf_trip.models import *
from bookie.models import *
from bookie.forms import BetTeeTimeForm


class EventHistoryView(ListView):
    model = Golf_Trip

# adds extra context to include the streamsong data for golfers and events. 
class HistoryStreamsong(TemplateView):
    template_name = 'golf_trip/trip_streamsong_index.html'
    extra_context={'golfers': Trip_Golfer.objects.all().filter(trip__trip_name='Streamsong'), 
                   'trip_events':Trip_Event.objects.all().filter(trip__trip_name='Streamsong')}


# sicne michigan is the current trip, the golfer and trip events are fitlered to just contain them.
class HomePage(TemplateView):
    template_name = 'golf_trip/trip_michigan_index.html'
    extra_context={'golfers': Trip_Golfer.objects.all().filter(trip__trip_name='Michigan'), 
                   'trip_events':Trip_Event.objects.all().filter(trip__trip_name='Michigan')}


#list details of the event
class EventDetailView(DetailView):
    model = Trip_Event
    template_name='golf_trip/golf_trip_detail.html'


# lsits all golfers on the michigan trip and orders them by first name
class PlayersListView(ListView):
    model = Trip_Golfer

    def get_queryset(self):
        queryset = Trip_Golfer.objects.all().filter(trip__trip_name='Michigan').order_by('golfer__first_name')
        
        return queryset

# 
class EventListView(ListView):
    model = Trip_Event

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(EventListView, self).get_context_data(**kwargs)
        # grabbing the dates for all of the events for the trip
        trip_dates = Trip_Event.objects.all().filter(trip__trip_name='Michigan').values('event_time').distinct()
        # grabbing all the courses for the trip
        trip_courses = Trip_Event.objects.all().filter(trip__trip_name='Michigan')

        context['trip_events'] = trip_courses
        context['trip_dates'] = trip_dates
        return context


class EventTeeTimeListView(ListView):
    model = Trip_TeeTime

    
    def get_queryset(self):
        queryset = Trip_TeeTime.objects.all().filter(tee_time_date=self.kwargs['event_day'])
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super(EventTeeTimeListView, self).get_context_data(**kwargs)
        # context['form'] = BetTeeTimeForm()
        return context


class EventTeeTimeDetailView(DetailView):
    model = Trip_TeeTime


class TeamListView(ListView):
    model = Trip_Team
    template_name = 'golf_trip/teams_list.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(TeamListView, self).get_context_data(**kwargs)
        # grabbing the dates for all of the events for the trip
        trip_teams = Trip_Team.objects.all().filter(trip__trip_name='Michigan')
        drafted = Trip_Team.objects.all().filter(trip__trip_name='Michigan').exclude(team="Not Drafted")
        not_drafted = Trip_Team.objects.all().filter(trip__trip_name='Michigan').filter(team="Not Drafted")


        context['trip_teams'] = trip_teams
        context['not_drafted'] = not_drafted
        context['drafted'] = drafted
        return context
    
class TripStandingsTemplateView(TemplateView):
    template_name = 'golf_trip/trip_standings.html'
    team_1_members = 'N/A'
    team_2_members = 'N/A'
    try:  
        teams = Trip_Team.objects.all().filter(trip__trip_name='Michigan')
        team_1_members = teams[0].members.all().order_by('-score')
        team_2_members = teams[1].members.all().order_by('-score')
        # team_1_members = Trip_TeamMember.objects.all().filter(team=teams[0]).order_by('-user__score')
        # team_2_members = Trip_TeamMember.objects.all().filter(team=teams[1]).order_by('-user__score')
    except:
        team_1_members = teams[2].members.all()
        team_2_members = teams[2].members.all()
    

    completed_rounds = Trip_TeeTime.objects.all().filter(teeTime_Complete=True)
    
    try:
        team_1 = teams[0]
        team_2 = teams[1]
    except:
        team_1 = 'N/A'
        team_2 = 'N/A'

    extra_context={'team_1': team_1, 'team_2': team_2,
                   'team_1_members': team_1_members,
                   'team_2_members': team_2_members,              
                   'trip_events':Trip_Event.objects.all().filter(trip__trip_name='Michigan'),
                   'completed_rounds': completed_rounds}