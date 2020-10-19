from django import forms
from django.contrib.auth.models import User
from .models import Profile, Post , Comment
from pyuploadcare.dj.forms import ImageField




class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ("image_name", "image_caption", "image",)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("comment",)