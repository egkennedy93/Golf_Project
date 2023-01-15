from Courses import views
from django.urls import path, include, re_path

app_name = 'courses'

urlpatterns = [
    # url for new course form. currently not being used.
    path(r'new/', views.CreateCourseView, name='course_new'),
    # lists all of the courses
    path(r'golf_course_list/', views.Golf_CourseListView.as_view(), name='golf_course_list'),
    # this is used when a tee is selected from the golf_course_list view
    re_path(r'golf_tee_list/(?P<pk>\d+)', views.Golf_TeeDetailView.as_view(), name='golf_tee_detail'),
    # not being used currently.
    re_path(r'golf_tee_list/new_tee/', views.Golf_TeeCreateView.as_view(), name='tee_new'),
]