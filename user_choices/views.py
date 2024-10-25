from django.shortcuts import render
from user_choices.models import UserChoice
from products.models import Product
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.shortcuts import get_object_or_404

# Create your views here.
def show_user_choices(request):
    return render(request, 'user_choices.html')
    
def add_user_choices(request, id):
    if request.method == 'POST':
        # Get the current logged-in user and the selected item
        current_user = request.user
        selected_item = Product.objects.get(pk=id)

        # Check if the choice already exists to prevent duplicates
        user_choice, created = UserChoice.objects.get_or_create(
            user=current_user,
            selected_item=selected_item
        )

        if created:
            # If the choice was created, show success'
            user_choice.save()
            return JsonResponse({'status': 'success', 'message': 'Choice added successfully.'})
        else:
            # If the choice already exists, show an error message
            return JsonResponse({'status': 'error', 'message': 'Choice already exists.'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})

def delete_user_choices(request, id):
    if request.method == 'DELETE':
        # Get the current logged-in user and the selected item
        current_user = request.user
        selected_item = get_object_or_404(Product, pk=id)

        try:
            # Try to find the user choice and delete it
            user_choice = UserChoice.objects.get(user=current_user, selected_item=selected_item)
            user_choice.delete()
            return JsonResponse({'status': 'success', 'message': 'Choice deleted successfully.'})
        except UserChoice.DoesNotExist:
            # If the user choice doesn't exist, show an error message
            return JsonResponse({'status': 'error', 'message': 'Choice does not exist.'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})

# @login_required
def show_user_choices_json(request):
    # Get all UserChoice entries for the logged-in user
    user_choices = UserChoice.objects.filter(user=request.user)
    
    # Manually build the JSON data with product details
    data = []
    for choice in user_choices:
        data.append({
            "id": choice.selected_item.pk,
            "category": choice.selected_item.category,
            "name": choice.selected_item.name,
            "price": choice.selected_item.price,
            "desc": choice.selected_item.desc,
            "color": choice.selected_item.color,
            "stock": choice.selected_item.stock,
            "shop_name": choice.selected_item.shop_name,
            "location": choice.selected_item.location,
            "img_url": choice.selected_item.img_url,
        })
    
    # Return the JSON response with the constructed data
    return JsonResponse(data, safe=False)