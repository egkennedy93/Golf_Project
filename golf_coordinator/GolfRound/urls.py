from GolfRound import views
from django.urls import path, re_path

app_name = 'round'

urlpatterns = [
    path(r'submit/', views.RoundSubmissionView, name='round_submit'),
    # path(r'round/<int:pk>', views.RoundDetailView.as_view(), name='round_detail'),
    # path('ajax/load-tees/', views.load_tees, name='ajax_load_tees'),  # <-- this one here
]
