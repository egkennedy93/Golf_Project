from GolfRound import views
from django.urls import path, re_path

app_name = 'round'

urlpatterns = [
    path(r'new/', views.CreateRoundView, name='round_new'),
]