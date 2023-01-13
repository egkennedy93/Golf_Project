from golf_trip import views
from django.urls import path, include, re_path

app_name = 'golf_trip'

urlpatterns = [
    
    path(r'', views.HomePage.as_view(), name='home'),
    path('history/', views.EventHistoryView.as_view(), name='event_history'),
    path('history/streamsong', views.HistoryStreamsong.as_view(), name='streamsong'),
    path ('events/', views.EventListView.as_view(), name='events_list'),
    path('events/<int:pk>', views.EventDetailView.as_view(), name='eventDetail'),
    path('players/', views.PlayersListView.as_view(), name='players_list'),
]