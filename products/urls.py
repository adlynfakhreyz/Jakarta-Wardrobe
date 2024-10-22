from django.urls import path
from products.views import show_products_by_price

app_name = 'products'

urlpatterns = [
    path('', show_products_by_price, name='show_products_by_price'),
]