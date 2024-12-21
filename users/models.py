from django.db import models
from django.contrib.auth.models import User

# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Menggunakan URLField dengan validator kustom
    avatar_url = models.URLField(max_length=500, default='https://i.pinimg.com/736x/50/42/90/504290aa11c08e6aa19831be382c8de2.jpg')  # Link gambar

    bio = models.TextField()

    def __str__(self):
        return self.user.username
