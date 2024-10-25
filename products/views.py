from django.shortcuts import render, get_object_or_404
from products.models import Product, Rating, Comment
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
from django.db.models import Avg
from user_choices.models import UserChoice

def show_products_by_price(request):
    products = Product.objects.annotate(avg_rating=Avg('rating__rating')).order_by('price')
    user_choices = list(UserChoice.objects.filter(user=request.user).values_list('selected_item_id', flat=True)) if request.user.is_authenticated else []
    
    context = {
        'products': products,
        'user_choices': user_choices,  # Pass UUIDs of user choices as a list
    }
    return render(request, 'product_page.html', context)

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

    if avg_rating is not None:
        avg_rating_int = int(round(avg_rating))
    else:
        avg_rating_int = 0

    return render(request, 'review_products.html', {
        'product': product,
        'avg_rating': avg_rating,
        'avg_rating_int': avg_rating_int,
        'ratings_with_users': ratings_with_users
    })

@login_required
@csrf_exempt
@require_POST
def add_rating(request):
    if request.method == 'POST':
        product_id = strip_tags(request.POST.get('product_id'))
        rating_value = strip_tags(int(request.POST.get('rating')))
        product = get_object_or_404(Product, uuid=product_id)

        rating_obj, created = Rating.objects.update_or_create(
            product=product,
            user=request.user,
            defaults={'rating': rating_value}
        )

        # Calculate new average rating
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
        Comment.objects.create(product=product, user=request.user, comment=comment_text)
        return JsonResponse({'message': 'Comment added successfully'})
    return JsonResponse({'message': 'Invalid request'}, status=400)

def get_ratings_comments(request, product_id):
    product = get_object_or_404(Product, uuid=product_id)
    ratings = product.rating_set.all()
    comments = product.comment_set.all()

    rating_list = list(ratings.values('rating', 'timestamp', 'user__username'))
    comment_list = list(comments.values('comment', 'timestamp', 'user__username'))

    return JsonResponse({'ratings': rating_list, 'comments': comment_list}, safe=False)