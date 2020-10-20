from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.home,name='instagram-home'),
    path('post/', views.post,name='post'),
    path('comment/', views.comment,name='comment'),
    url(r'^like/(\d+)',views.postlike, name="postlike"),
    path('followers/', views.followers,name='followers'),
]
