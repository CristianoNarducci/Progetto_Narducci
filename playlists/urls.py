from django.urls import path
from django.contrib.auth import views as auth_views
from songs import views as songs
from . import views

app_name = 'playlists'

urlpatterns = [
    path('signup/', views.signUpView, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login.as_view(), name='login'),
    path('', views.example.as_view(), name='home'),
    path("accounts/login/",auth_views.LoginView.as_view(template_name="registration/login.html"),name="login"),
]
