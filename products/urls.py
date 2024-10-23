from django.urls import path
from products.views import show_products_by_price
from . import views

app_name = 'products'

urlpatterns = [
    path('', show_products_by_price, name='show_products_by_price'),
    path('detail/<uuid:product_id>/', views.product_detail, name='product_detail'),
]