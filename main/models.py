from django.db import models
from django.contrib.auth.models import User
import uuid

class ItemEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    rating = models.IntegerField()
    location = models.CharField(max_length=255) 
    kategories = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

