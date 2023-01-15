from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = 'accounts'
urlpatterns = [
    # users login form
    path('login/', auth_views.LoginView.as_view(), name='login'),
    # users logout form
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    # users can sign up and register for the site. 
    path('signup/', views.register, name='signup'),
]

