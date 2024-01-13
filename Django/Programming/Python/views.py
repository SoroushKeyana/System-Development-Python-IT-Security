from django.shortcuts import render, redirect
from .models import User
from .forms import UserProfileForm

def index(request):
    return render(request, 'Python/index.html', {'key': 'something'})

def user_list(request):
    users = User.objects.all()
    return render(request, 'Python/user_list.html', {'users': users})

def user_form(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserProfileForm()
    
    return render(request, 'Python/user_form.html', {'form': form})
