from django.urls import path
from . import views
from products.views import show_three_products

app_name = 'main'

urlpatterns = [
    path('', show_three_products, name='show_three_products'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('', views.show_main , name='show_main'),
]