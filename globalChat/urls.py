from django.urls import path
from . import views

app_name = 'globalChat'

urlpatterns = [
    path('', views.global_chat, name='global_chat'),  # Routing untuk Global Chat page
    path('new/', views.new_forum, name='new_post'), 
    path('forum/<int:forum_id>/', views.detail_chat, name='detail_chat'),  # Routing untuk detail chat
    path('forum/edit/<int:id>/', views.edit_forum, name='edit_forum'),
    path('forum/delete/<int:id>/', views.delete_forum, name='delete_forum'),
    path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('forum/<int:forum_id>/like/', views.toggle_like_forum, name='toggle_like_forum'),
    path('forum/<int:forum_id>/bookmark/', views.toggle_bookmark, name="toggle_bookmark"),
    
]
