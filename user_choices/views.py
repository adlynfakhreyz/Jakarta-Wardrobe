from django.shortcuts import render
from user_choices.models import UserChoice


# Create your views here.
def show_user_choices(request):
    return render(request, 'user_choices.html')

def delete_user_choices(request, id):
    pass
    
def add_user_choices(request, id):
    new_user_choice = UserChoice(user_id=id, choice=request.POST['choice'])