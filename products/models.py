from django.db import models
import uuid
from main.models import ItemEntry  # Impor ItemEntry dari app 'main'
from django.contrib.auth.models import User  # Impor User


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
    
class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_id = models.ForeignKey(ItemEntry, on_delete=models.CASCADE)
    comment_text = models.TextField(max_length=1500)
    timestamp = models.DateTimeField(auto_now_add=True)  # Menambahkan timestamp


