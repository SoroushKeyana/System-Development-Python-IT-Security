from django.shortcuts import render, redirect
from .forms import SignUpForm, PostForm
from .models import Post
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Post, UserProfile
from .forms import PostForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse


def home(request):    
    return render(request, 'index.html', {'key': 'Always here for you'})

def thanks(request):
    return render(request, 'thanks.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('thanks')
    else:
        form = SignUpForm()

    # Handle the case when form validation fails
    return render(request, 'signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'signin.html', {'form': form})

@login_required
def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

@login_required
def post_list(request):
    posts = Post.objects.all()

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            author = request.user
            Post.objects.create(title=title, content=content, author=author)
            return redirect('post_list')
    else:
        form = PostForm()

    return render(request, 'post_list.html', {'form': form, 'posts': posts})