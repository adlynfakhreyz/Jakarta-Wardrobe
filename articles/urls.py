from django.urls import path
from . import views

urlpatterns = [
    path('list_article', views.list_articles, name='list_articles'),  # /articles/
    path('<uuid:article_id>/', views.article_detail, name='article_detail'),  # /articles/<uuid>
    path('add/', views.add_article, name='add_article'),  # /articles/add/
    path('delete/<uuid:article_id>/', views.delete_article, name='delete_article'),
]
