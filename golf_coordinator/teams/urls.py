from django.urls import path, re_path
from . import views

app_name = 'teams'



urlpatterns = [
    path('', views.ListTeam.as_view(), name='all'),
    path('new/', views.CreateTeam.as_view(), name='create'),
    # re_path('rounds/in/(?P<team>[-\w]+)/', views.SingleGroup.as_view(), name='single'),
]