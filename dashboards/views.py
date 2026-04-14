
from django.shortcuts import render, redirect
from blogs.models import Category, Blog
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm
from django.shortcuts import get_object_or_404

# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    category_count=Category.objects.all().count()
    blog_count=Blog.objects.all().count()
    
    context={
        'category_count': category_count,
        'blog_count': blog_count
    }
    return render(request, 'dashboard/dashboard.html', context)

def categories(request):
    categories=Category.objects.all()
    context={
        'categories': categories
    }
    return render(request, 'dashboard/categories.html', context)

def add_categories(request):
    if request.method=='POST':
        form=CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form=CategoryForm()
    context={
        'form': form
    }
    return render(request, 'dashboard/add_categories.html', context)

def edit_categories(request, pk):
    category=get_object_or_404(Category, pk=pk)
    if request.method=='POST':
        form=CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form=CategoryForm(instance=category)
    context={
        'form': form,
        'category': category
    }
    return render(request, 'dashboard/edit_categories.html', context)

def delete_categories(request, pk):
    category=get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('categories')
    