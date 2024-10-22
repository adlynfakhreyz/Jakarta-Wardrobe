from django.urls import path
from user_choices.views import show_user_choices

app_name = 'user_choices'

urlpatterns = [
    path('', show_user_choices, name='show_user_choices'),
]