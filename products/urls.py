from django.urls import path
from .views import (
    show_products_by_price,
    review_products,
    submit_rating,
    submit_comment,
    get_ratings_comments
)

app_name = 'products'

urlpatterns = [
    path('', show_products_by_price, name='show_products_by_price'),
    path('review_products/<uuid:id>/', review_products, name='review_products'),
    path('submit_rating/', submit_rating, name='submit_rating'),
    path('submit_comment/', submit_comment, name='submit_comment'),
    path('get_ratings_comments/<uuid:product_id>/', get_ratings_comments, name='get_ratings_comments'),
]
