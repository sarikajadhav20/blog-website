from django.shortcuts import redirect, render
from blogs.models import Category, Blog
from .forms import RegistrationForm
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm

def home(request):
    categories = Category.objects.all()
    featured_post = Blog.objects.filter(is_featured=True)
    posts=Blog.objects.filter(is_featured=False,status='1')

    context = {
        'categories': categories,
        'featured_post': featured_post,
        'posts': posts,

    }

    return render(request, 'home.html', context)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home page after successful registration
    else:   
       form=RegistrationForm()
    context={
        'form':form
    }
    
    return render(request, 'register.html', context)


#Login
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')  # Redirect to dashboard after successful login
    else:
        form = AuthenticationForm()
    context={
        'form': form
    }
    return render(request, 'login.html',context)

#Logout
def logout(request):
    auth.logout(request)
    return redirect('home')                 
