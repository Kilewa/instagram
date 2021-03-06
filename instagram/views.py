from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
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
        'posts': posts,
    }
    return render(request, 'instagram/home.html', context,)


def post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('instagram-home')
    else:
        form = PostForm()
    return render(request, 'instagram/post.html', {'form': form})


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


def postlike(request, image_id):

    liked_image = Post.objects.get(pk=image_id)

    is_liked = 0
    if liked_image.likes.filter(id=request.user.id).exists():
        liked_image.likes.remove(request.user)
        is_liked += 1
    else:
        liked_image.likes.add(request.user)
        is_liked = True
        return render(request, 'instagram/home.html')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def comment(request, post_id):
    post = Post.get_image_by_id(post_id)
    post_comments = Comment.objects.filter(image=post)
    if request.method == "POST":
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.profile = Profile.get_profile_by_userid(request.user.id)
            comment.image = post
            comment.save()
            comment_form = CommentForm()
            Post.objects.filter(id=post_id).update(comments=F("comments") + 1)
            messages.success(request, f'Comment successfully added')
            return redirect("post", post_id)
    else:
        comment_form = CommentForm()
    context = {
        'profile': request.user.profile,
        'post': post,
        'form': comment_form,
        'comments': post_comments,
    }
    return render(request, 'instagram/home.html', context)
