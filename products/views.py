from django.shortcuts import render
from .models import Product
from django.views.generic import ListView
from django.http import JsonResponse
from .models import Product  # Pastikan model yang benar digunakan

# Create your views here.
def show_products_by_price(request):
    products = Product.objects.order_by('price')
    return render(request, 'product_page.html', {'products': products})

def get_products_by_category(request, category):
    products = Product.objects.filter(category=category).values('id', 'name', 'price', 'img_url', 'description')
    return JsonResponse(list(products), safe=False)

def show_products_by_category(request, category):
    products = Product.objects.filter(category=category)
    products_data = list(products.values())
    return JsonResponse(products_data, safe=False)

def show_men_products(request):
    products = Product.objects.filter(category='Men')
    return JsonResponse(list(products.values()), safe=False)

def show_women_products(request):
    products = Product.objects.filter(category='Women')
    return render(request, 'product_page.html', {'products': products})

def show_footwear_products(request):
    products = Product.objects.filter(category='Footwear')
    return render(request, 'product_page.html', {'products': products})

def show_three_products(request):
    products = Product.objects.all()[:3]
    return render(request, 'main.html', {'products': products})

def product_detail(request, product_id):
    try:
        product = Product.objects.get(uuid=product_id)
        response_data = {
            'name': product.name,
            'category': product.category,
            'price': product.price,
            'description': product.desc,
            'color': product.color,
            'stock': product.stock,
            'shop_name': product.shop_name,
            'location': product.location,
            'img_url': product.img_url,  # Tambahkan gambar produk
        }
        return JsonResponse(response_data)
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Produk tidak ditemukan'}, status=404)
