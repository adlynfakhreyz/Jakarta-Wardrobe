from django.db import models
import uuid
from main.models import ItemEntry  
from django.contrib.auth.models import User  

class Product(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    desc = models.TextField(blank=True, null=True)
    color = models.CharField(max_length=50)
    stock = models.IntegerField()
    shop_name = models.CharField(max_length=200)
    location = models.CharField(max_length=255)
    img_url = models.URLField(max_length=500)

    def __str__(self):
        return f"{self.name} - {self.category}"

class Rating(models.Model):
    RATING_CHOICES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    )

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
