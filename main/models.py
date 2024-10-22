from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class ItemEntry:
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    rating = models.IntegerField()
    location = models.CharField(max_length=255) 
    kategories = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

RATING = [
    (1, '$'),
    (2, '$$'),
    (3, '$$$'),
    (4, '$$$$'),
    (5, '$$$$$')
]

class Rating(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_id = models.ForeignKey(ItemEntry, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    rating_value = models.IntegerField(null=True, blank=True, choices = RATING)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
class Rate(models.Model):
    source=models.CharField(max_length=50)
    rating=models.CharField(max_length=10)

    def __str__(self):
        return self.source
