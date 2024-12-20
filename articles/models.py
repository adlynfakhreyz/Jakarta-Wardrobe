from django.db import models

# Create your models here.
from django.db import models
import uuid
from django.contrib.auth.models import User

class Article(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    image_url = models.URLField(max_length=500)  # Link gambar
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
