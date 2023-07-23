from golf_trip import views
from django.urls import path, include, re_path

app_name = 'golf_trip'

urlpatterns = [
    
    path(r'', views.HomePage.as_view(), name='home'),
    # look back on previous trips
    path('history/', views.EventHistoryView.as_view(), name='event_history'),
    # if the user selects to see streamsong data
    path('history/streamsong', views.HistoryStreamsong.as_view(), name='streamsong'),
    # if it's a current trip, all events are shown by the day
    path('events/', views.EventListView.as_view(), name='events_list'),
    # if the event day is selected, that day's courses and tee times are displayed.
    re_path(r'^events/(?P<event_day>\d{4}-\d{2}-\d{2})/$', views.EventTeeTimeListView.as_view(), name='event_teetime'),
    # currently not being used, but intended to show details of the event
    path(r'^teetime/<int:pk>', views.EventTeeTimeDetailView.as_view(), name='teetime_detail'),
    path('events/<int:pk>', views.EventDetailView.as_view(), name='eventDetail'),
    # Lists all players on the trip
    path('players/', views.PlayersListView.as_view(), name='players_list'),
    path('players/<int:pk>', views.PlayersDetailView.as_view(), name='player_detail'),
    path('teams/', views.TeamListView.as_view(), name='team_list'),
    path('standings/', views.TripStandingsTemplateView.as_view(), name='trip_standings'),
]