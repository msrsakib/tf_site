"""TechFizzer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/

"""
from django.contrib import admin
from django.urls import path, include
from users import views as views_user
from django.contrib.auth import views as views_auth
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # admin page
    path('register/', views_user.register, name='register'),  # register page
    path('profile/', views_user.profile, name='profile'),
    path('login/', views_auth.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', views_auth.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', include('blog.urls')),  # home page

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
