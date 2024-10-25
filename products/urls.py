from django.urls import path
from products.views import show_products_by_price, show_products_by_category,show_three_products
from . import views

app_name = 'products'

urlpatterns = [
    path('', show_products_by_price, name='show_products_by_price'),
    path('detail/<uuid:product_id>/', views.product_detail, name='product_detail'),
    path('product/<uuid:product_id>/', views.product_detail, name='product_detail'),
    path('api/products/category/<str:category>/', views.get_products_by_category, name='get_products_by_category'),
]