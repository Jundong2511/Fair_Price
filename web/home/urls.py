from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    )

urlpatterns = [
    path('', views.PostListView.as_view(),name="main_home"),
    # pk means primary key, int: means pk have to be a integer.
    path('post/<int:pk>', views.PostDetailView.as_view(),name="post_detail"),
    path('post/new', views.PostCreateView.as_view(),name="post_create"),
    path('post/<int:pk>/update', views.PostUpdateView.as_view(),name="post_update"),
    path('about/', views.about, name='main_about'),
    path('post/<int:pk>/delete', views.PostDeleteView.as_view(),name="post_delete"),
    path('user/<str:username>', views.UserPostListView.as_view(),name="user_posts"),


]
