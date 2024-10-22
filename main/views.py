from django.shortcuts import render, redirect
from main.models import ItemEntry
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User
import uuid


# Create your views here.
def show_main(request):
    return render(request, 'main.html')

