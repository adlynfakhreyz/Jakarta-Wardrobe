from django.urls import path
from .views import profile, profile_json
from users.views import ResetPasswordView
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'users'

urlpatterns = [
    path('', profile, name='profile'),
    path('json/', profile_json, name='profile_json'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)