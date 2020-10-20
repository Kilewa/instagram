from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Post, User, Comment, Profile
from . forms import CommentForm, PostForm
from friendship.models import Friend, Follow, Block
# from .email import send_welcome_email



# def news_today(request):
#     if request.method == 'POST':
#         form = NewsLetterForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['your_name']
#             email = form.cleaned_data['email']

#             recipient = NewsLetterRecipients(name = name,email =email)
#             recipient.save()
#             send_welcome_email(name,email)

#             HttpResponseRedirect('home')
#             #.................
#     return render(request, 'instagram/home.html')


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

def comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('instagram-home')
    else:        
        form = CommentForm()
    return render(request, 'instagram/comment.html', {'form': form}) 


def followers(request):
    followers = Follow.objects.followers(request.user)
    following = Follow.objects.following(request.user)
    # following_created = Following.objects.add_follower(request.user, other_user)

    context = {
        'followers': followers,
        'following': following,
        # 'following_created':following_created
    }

    return render(request, 'instagram/followers.html', context)