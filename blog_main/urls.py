from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from blogs import views as blog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('category/', include('blogs.urls')),
    path('blog/<slug:slug>/', blog_views.blog_detail, name='blog_detail'),
    path('blog/search/', blog_views.search, name='search'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', include('dashboards.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
