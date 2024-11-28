# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment, Topic
from .forms import PostForm, CommentForm, TopicForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def forum(request):
    topics = Topic.objects.all()
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('forum')
    else:
        form = TopicForm()

    return render(request, 'forum.html', {'topics': topics, 'form': form})


# forum/views.py
@login_required(login_url='login')
def topic_detail(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    posts = topic.posts.all()

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.author = request.user
            post.save()
            return redirect('topic_detail', topic_id=topic.id)
    else:
        form = PostForm()

    return render(request, 'topic_detail.html', {'topic': topic, 'posts': posts, 'form': form})

@login_required(login_url='login')
def create_topic(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        topic = Topic.objects.create(name=name)
        return redirect('forum')
    return render(request, 'create_topic.html')
@login_required(login_url='login')
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', post_id=post.id)
    else:
        comment_form = CommentForm()
    return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form})

@login_required(login_url='login')
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('forum')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

@login_required(login_url='login')
def create_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = CommentForm()
    return render(request, 'create_comment.html', {'form': form, 'post': post})