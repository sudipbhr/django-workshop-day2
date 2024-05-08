from django.urls import path
from blog import views



urlpatterns = [
    path('', views.home),
    path('posts/', views.posts),
    path('post-detail/', views.post_detail),
]
