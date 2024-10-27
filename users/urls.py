from django.urls import path
from .views import profile
from users.views import ResetPasswordView
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path('profile/', profile, name='profile'),
]