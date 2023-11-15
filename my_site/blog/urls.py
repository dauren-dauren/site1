from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('posts/', views.posts, name='blog-posts'),
    path('create/', views.create, name='blog-create'),
    path('posts/<int:post_id>/', views.edit_post, name='post'),
    ]