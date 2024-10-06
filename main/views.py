from django.shortcuts import render, redirect
from main.models import ItemEntry
from django.contrib.auth.models import User
import uuid
# Create your views here.
def show_main(request):
    return render(request, 'main.html')

