from django.contrib import admin
from . models import Category, Blog

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','category_name', 'created_at', 'updated_at')

class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'category', 'author','blog_image', 'status', 'is_featured', 'created_at', 'updated_at')    
    prepopulated_fields = {'slug':('title',)}
    search_fields = ('id','title', 'category__category_name', 'author__username')
    list_editable=('status', 'is_featured')
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)
