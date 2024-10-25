from django.urls import path
from . import views
from products.views import show_best_10_products

app_name = 'main'

urlpatterns = [
    path('', show_best_10_products, name='show_best_10_products'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('', views.show_main , name='show_main'),
]