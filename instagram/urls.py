from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='instagram-home'),
    path('post/', views.post,name='instagram-post'),
]
