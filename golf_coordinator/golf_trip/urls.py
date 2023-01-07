from golf_trip import views
from django.urls import path, include, re_path

app_name = 'golf_trip'

urlpatterns = [
    
    path(r'', views.HomePage.as_view(), name='trip_2023'),
]