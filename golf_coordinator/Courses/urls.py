from Courses import views
from django.urls import path, include, re_path

app_name = 'courses'

urlpatterns = [
    path(r'new/', views.CreateCourseView, name='course_new'),
]