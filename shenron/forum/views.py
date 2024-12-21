from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment, Topic
from django.contrib.auth.decorators import login_required

from notifications.models import Notifications

@login_required(login_url='login')
def forum(request):
    if not request.user.activated:
        return redirect('activate_account')
    topics = Topic.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            Topic.objects.create(name=name, createdby=request.user)
            return redirect('forum')
    return render(request, 'forum.html', {'topics': topics})


@login_required(login_url='login')
def topic_detail(request, topic_id):
    if not request.user.activated:
        return redirect('activate_account')
    topic = get_object_or_404(Topic, id=topic_id)
    posts = topic.posts.all()
    if request.method == 'POST':
        if 'follow' in request.POST:
            if request.user in topic.followers.all():
                topic.followers.remove(request.user)
            else:
                topic.followers.add(request.user)
            return redirect('topic_detail', topic_id=topic.id)
        if 'delete_topic' in request.POST and (topic.createdby == request.user or request.user.has_perm('forum.delete_topic')):
            topic.delete()
            return redirect('forum')
        title=request.POST.get('title')
        content=request.POST.get('content')
        if title and content:
            post=Post.objects.create(title=title, content=content, author=request.user, topic=topic)
            followers = topic.followers.exclude(id=request.user.id)
            for follower in followers:
                Notifications.objects.create(
                    user=follower,
                    message=f'New post by {request.user.username} in {topic.name}: {title}',
                    post=post
                )
            return redirect('topic_detail', topic_id=topic.id)
    return render(request, 'topic_detail.html', {'topic': topic, 'posts': posts})

@login_required(login_url='login')
def post_detail(request, post_id):
    if not request.user.activated:
        return redirect('activate_account')
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()
    print(request.user.get_all_permissions())
    if request.method == 'POST':
        if 'delete_post' in request.POST and (post.author == request.user or request.user.has_perm('forum.delete_post')):
            post.delete()
            return redirect('forum')
        if 'delete_comment' in request.POST:
            comment_id = request.POST.get('comment_id')
            comment = get_object_or_404(Comment, id=comment_id)
            if comment.author == request.user or request.user.has_perm('forum.delete_comment'):
                comment.delete()
            return redirect('post_detail', post_id=post.id)
        comment= request.POST.get('comment')
        if comment:
            comment_obj=Comment.objects.create(content=comment, author=request.user, post=post)
            if post.author != request.user:
                Notifications.objects.create(
                    user=post.author,
                    message=f'New comment on your post "{post.title}" by {request.user.username}',
                    post= post
                )
            return redirect('post_detail', post_id=post.id)
    return render(request, 'post_detail.html', {'post': post, 'comments': comments})


