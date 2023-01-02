from Courses import views
from django.urls import path, include, re_path

app_name = 'courses'

urlpatterns = [
    path(r'new/', views.CreateCourseView, name='course_new'),
    path(r'golf_course_list/', views.Golf_CourseListView.as_view(), name='golf_course_list'),
    re_path(r'golf_course_list/(?P<pk>\d+)', views.Golf_CourseDetailView.as_view(), name='golf_course_detail'),
    re_path(r'golf_tee_list/(?P<pk>\d+)', views.Golf_TeeDetailView.as_view(), name='golf_tee_detail'),
    re_path(r'golf_tee_list/new_tee/', views.Golf_TeeCreateView.as_view(), name='tee_new'),
]