from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Post, User, Comment, Profile
from . forms import CommentForm, PostForm
from friendship.models import Friend, Follow, Block



@login_required
def home(request):
    posts = Post.get_all_images()
    context = {
        'posts': posts
    }
    return render(request, 'instagram/home.html', context)



def post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('instagram-home')
    else:        
        form = PostForm()
    return render(request, 'instagram/post.html', {'form': form}) 
