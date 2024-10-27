from django.urls import path
from . import views
from products.views import show_best_10_products
from . import views

app_name = 'main'

urlpatterns = [
    path('', show_best_10_products, name='show_best_10_products'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),  
    path('terms_of_service/', views.terms_of_service, name='terms_of_service'), 
    path('contact_us/', views.contact_us, name='contact_us'), 
    path('', views.show_main , name='show_main'),
]