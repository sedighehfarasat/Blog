from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostListView.as_view(), name='blog-list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='blog-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='blog-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='blog-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='blog-delete'),
    path('user/<str:username>/', views.UserPostListView.as_view(), name='blog-user-posts'),
]
