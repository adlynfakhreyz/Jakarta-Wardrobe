from django.urls import path
from main.views import show_main, register, login_user, logout_user, privacy_policy
from . import views

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),  
    path('terms_of_service/', views.terms_of_service, name='terms_of_service'), 
    path('contact_us/', views.contact_us, name='contact_us'), 

]