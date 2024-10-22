from django.db import models
import uuid

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

