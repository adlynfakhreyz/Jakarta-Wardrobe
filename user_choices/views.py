from django.shortcuts import render

# Create your views here.
def show_user_choices(request):
    return render(request, 'user_choices.html')