from bookie import views
from django.urls import path, include, re_path
from bookie.views import BetPVPCreateView, BetTVTCreateView

app_name = 'bookie'

urlpatterns = [
    path('player_bet/', BetPVPCreateView.as_view(), name='bet_pvp')
    # url for new course form. currently not being used.
    # path(r'new/', views.CreateCourseView, name='course_new'),
   
]