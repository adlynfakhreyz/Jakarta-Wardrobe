from django.shortcuts import render, get_object_or_404
from products.models import Product, Rating, Comment
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Avg

def show_products_by_price(request):
    products = Product.objects.order_by('price')
    return render(request, 'product_page.html', {'products': products})

def review_products(request, id):
    product = get_object_or_404(Product, uuid=id)
    avg_rating = Rating.objects.filter(product=product).aggregate(Avg('rating'))['rating__avg']
    if avg_rating is not None:
        avg_rating_int = int(round(avg_rating))
    else:
        avg_rating_int = 0
    return render(request, 'review_products.html', {
        'product': product,
        'avg_rating': avg_rating,
        'avg_rating_int': avg_rating_int
    })

@login_required
def submit_rating(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        rating_value = int(request.POST.get('rating'))
        product = get_object_or_404(Product, uuid=product_id)

        # Update or create rating
        rating_obj, created = Rating.objects.update_or_create(
            product=product,
            user=request.user,
            defaults={'rating': rating_value}
        )

        # Calculate new average rating
        avg_rating = Rating.objects.filter(product=product).aggregate(Avg('rating'))['rating__avg']
        return JsonResponse({
            'message': 'Rating submitted successfully',
            'avg_rating': avg_rating
        })
    return JsonResponse({'message': 'Invalid request'}, status=400)

@login_required
def submit_comment(request):
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
