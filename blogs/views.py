from django.shortcuts import render,HttpResponse
from .models import Blog,Category

def post_by_category(request, category_id):
    posts=Blog.objects.filter(status='1',category=category_id)
    try:
        category=Category.objects.get(id=category_id)
    except Category.DoesNotExist:
        return HttpResponse("Category not found", status=404)
    
    context={
        'posts':posts,
        'category':category,
    }
    
    return render(request, 'posts_by_category.html', context)


# Create your views here.
def blog_detail(request, slug):
    try:
        post = Blog.objects.get(slug=slug, status='1')
    except Blog.DoesNotExist:
        return HttpResponse("Blog post not found", status=404)
    
    context = {
        'post': post,
    }
    
    return render(request, 'blog_detail.html', context)


#search functionality
def search(request):
    query = request.GET.get('keyword', '')
    results = Blog.objects.filter(title__icontains=query, status='1')
    
    context = {
        'results': results,
        'query': query,
    }
    
    return render(request, 'search.html', context)
 