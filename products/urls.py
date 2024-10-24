from django.urls import path
from .views import show_products_by_price, review_products, add_rating, add_comment, get_ratings_comments
from . import views 
app_name = 'products'

urlpatterns = [
    path('', show_products_by_price, name='show_products_by_price'),
    path('review_products/<uuid:id>/', review_products, name='review_products'),
    path('add_rating/', add_rating, name='add_rating'),
    path('add_comment/', add_comment, name='add_comment'),
    path('get_ratings_comments/<uuid:product_id>/', get_ratings_comments, name='get_ratings_comments'),
    path('detail/<uuid:product_id>/', views.product_detail, name='product_detail'),
]
