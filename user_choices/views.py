from django.shortcuts import render
from user_choices.models import UserChoice
from products.models import Product, Rating
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.db.models import Avg, F
from django.shortcuts import get_object_or_404,  render, redirect
from django.contrib.auth.decorators import login_required
from .forms import NotesForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@login_required(login_url='/login')
def show_user_choices(request):
    return render(request, 'user_choices.html')


@login_required(login_url='/login')
@csrf_exempt
def add_user_choices(request, id):
    if not request.user.is_authenticated:
        # Return a JSON response if the user is not authenticated
        return JsonResponse({'status': 'error', 'message': 'User is not authenticated.'}, status=401)

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

@login_required(login_url='/login')
@csrf_exempt
def delete_user_choices(request, id):
    if request.method == 'DELETE' or request.method == 'POST':
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

@login_required(login_url='/login')
def show_user_choices_json(request):
    # Filter products selected by the logged-in user and annotate with average rating
    user_products = Product.objects.filter(userchoice__user=request.user).annotate(
        avg_rating=Avg('rating__rating'),
        notes=F('userchoice__notes')  # Adjust field name if different
    ).values(
        'uuid',
        'category',
        'name',
        'price',
        'desc',
        'color',
        'stock',
        'shop_name',
        'location',
        'img_url',
        'avg_rating',
        'notes'
    )

    # Return the JSON response with the constructed data
    return JsonResponse(list(user_products), safe=False)

@login_required
def edit_notes(request, id):
    """
    View for editing notes for a specific product.
    Creates a new UserChoice if it doesn't exist.
    """
    selected_item = Product.objects.get(pk=id)
    user_choice, created = UserChoice.objects.get_or_create(
        user=request.user,
        selected_item=selected_item,
        defaults={'notes': ''}
    )

    if request.method == 'POST':
        form = NotesForm(request.POST, instance=user_choice)
        if form.is_valid():
            form.save()
            return redirect('/user_choices')  # Adjust this to your product detail URL name
    else:
        form = NotesForm(instance=user_choice)
        
    context = {
        'form': form,
        'product': selected_item
    }
    return render(request, 'edit_notes.html', context)