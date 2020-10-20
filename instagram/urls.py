from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='instagram-home'),
    path('post/', views.post,name='instagram-post'),
    path('comment/', views.comment,name='instagram-comment'),
    path('followers/', views.followers,name='instagram-followers'),
]
