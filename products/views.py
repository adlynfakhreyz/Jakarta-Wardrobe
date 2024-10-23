from django.shortcuts import render
from .models import Product
from django.views.generic import ListView
# Create your views here.
def show_products_by_price(request):
    products = Product.objects.order_by('price')
    return render(request, 'product_page.html', {'products': products})