from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.
class UserChoice(models.Model):
    """
    Model untuk menyimpan pilihan pengguna terkait produk.

    Attributes:
        user (User): Pengguna yang membuat pilihan.
        selected_item (Product): id item yang dipilih oleh pengguna.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    selected_item = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'selected_item') # Menetapkan constraint unik antara user dan produk