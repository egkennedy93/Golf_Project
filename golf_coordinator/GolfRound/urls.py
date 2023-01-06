from GolfRound import views
from django.urls import path, re_path

app_name = 'round'

urlpatterns = [
    path(r'submit/', views.CreateRoundSubmissionView.as_view(), name='round_submit'),
    path(r'new/<int:pk>', views.CreateRoundView, name='round_new'),
    path('ajax/load-tees/', views.load_tees, name='ajax_load_tees'),  # <-- this one here
]
