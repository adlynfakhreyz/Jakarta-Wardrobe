from django.shortcuts import render, get_object_or_404
from products.models import Product, Rating, Comment
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
from django.db.models import Avg
from django.utils import timezone

def show_products_by_price(request):
    products = Product.objects.annotate(avg_rating=Avg('rating__rating')).order_by('price')
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


def review_products(request, id):
    product = get_object_or_404(Product, uuid=id)
    avg_rating = Rating.objects.filter(product=product).aggregate(Avg('rating'))['rating__avg']
    ratings_with_users = Rating.objects.filter(product=product).select_related('user').order_by('-timestamp')
    comments = Comment.objects.filter(product=product).select_related('user').order_by('-timestamp')


    if avg_rating is not None:
        avg_rating_int = int(round(avg_rating))
    else:
        avg_rating_int = 0

    return render(request, 'review_products.html', {
        'product': product,
        'avg_rating': avg_rating,
        'avg_rating_int': avg_rating_int,
        'ratings_with_users': ratings_with_users,
        'comments': comments
        
    })

@login_required
@csrf_exempt
@require_POST
def add_rating(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        rating_value = int(request.POST.get('rating'))
        product = get_object_or_404(Product, uuid=product_id)

        # Buat atau perbarui rating
        rating_obj, created = Rating.objects.update_or_create(
            product=product,
            user=request.user,
            defaults={'rating': rating_value}
        )

        # Jika rating diperbarui, perbarui juga timestamp-nya
        if not created:
            rating_obj.timestamp = timezone.now()
            rating_obj.save()  # Simpan instance secara eksplisit

        # Hitung rating rata-rata terbaru
        avg_rating = Rating.objects.filter(product=product).aggregate(Avg('rating'))['rating__avg']
        ratings_with_users = Rating.objects.filter(product=product).select_related('user').order_by('-timestamp')

        ratings_data = [{
            'user': rating.user.username,
            'rating': rating.rating,
            'timestamp': rating.timestamp.strftime("%d %B %Y, %H:%M")
        } for rating in ratings_with_users]

        return JsonResponse({
            'message': 'Rating added successfully',
            'avg_rating': avg_rating,
            'ratings_with_users': ratings_data
        }, status=201)

    return JsonResponse({'message': 'Invalid request'}, status=400)
@login_required
@csrf_exempt
@require_POST
def add_comment(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        comment_text = request.POST.get('comment')
        product = get_object_or_404(Product, uuid=product_id)
        new_comment = Comment.objects.create(product=product, user=request.user, comment=comment_text)
        
        # Mengembalikan respons dengan data komentar yang baru
        return JsonResponse({
            'message': 'Comment added successfully',
            'user': new_comment.user.username,
            'comment': new_comment.comment,
            'timestamp': new_comment.timestamp.strftime("%d %B %Y, %H:%M")
        }, status=201)
    return JsonResponse({'message': 'Invalid request'}, status=400)

def get_ratings_comments(request, product_id):
    product = get_object_or_404(Product, uuid=product_id)
    ratings = product.rating_set.all()
    comments = product.comment_set.all()

    rating_list = list(ratings.values('rating', 'timestamp', 'user__username'))
    comment_list = list(comments.values('comment', 'timestamp', 'user__username'))

    return JsonResponse({'ratings': rating_list, 'comments': comment_list}, safe=False)