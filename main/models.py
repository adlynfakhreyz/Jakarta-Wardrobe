from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class ItemEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    rating = models.IntegerField()
    location = models.CharField(max_length=255) 
    kategories = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_id = models.ForeignKey(ItemEntry, on_delete=models.CASCADE)
    comment_text = models.TextField(max_length=1500)
    timestamp = models.DateTimeField(auto_now_add=True)  # Menambahkan timestamp
