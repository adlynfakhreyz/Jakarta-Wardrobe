from django.shortcuts import render
from .models import Product
from django.views.generic import ListView
from django.http import JsonResponse
from .models import Product  # Pastikan model yang benar digunakan
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponseBadRequest
from .models import Product, Review
from django.contrib.auth.decorators import login_required


# Create your views here.
def show_products_by_price(request):
    products = Product.objects.order_by('price')
    return render(request, 'product_page.html', {'products': products})

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
    

@login_required
def add_review(request, product_uuid):
    if request.method == 'POST':
        product = get_object_or_404(Product, uuid=product_uuid)
        comment_text = request.POST.get('comment_text')

        if not comment_text:
            return HttpResponseBadRequest('Comment cannot be empty')

        Review.objects.create(
            user=request.user,
            item_id=product,
            comment_text=comment_text
        )

        return JsonResponse({'message': 'Review added successfully'})
    else:
        return HttpResponseBadRequest('Invalid request method')

