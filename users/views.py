from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from .forms import UpdateUserForm, UpdateProfileForm
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import JsonResponse


@login_required
@csrf_exempt
# @require_POST
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'message': 'Your profile is updated successfully'}, status=200)
            messages.success(request, 'Your profile is updated successfully')
            return redirect('users:profile')
        else:
             if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                errors = {
                    'user_form_errors': user_form.errors,
                    'profile_form_errors': profile_form.errors
                }
                return JsonResponse(errors, status=400)
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)
        return render(request, 'users/profile.html', {'user_form': user_form, 'profile_form': profile_form})


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('users-home')

def profile_json(request):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'You must be logged in to view this data.'}, status=401)
    
    data = {
        'username': request.user.username,
        'profile_picture': request.user.profile.avatar.url if request.user.profile.avatar else None
    }
    return JsonResponse(data)