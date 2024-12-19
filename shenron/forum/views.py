from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment, Topic
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view


@login_required(login_url='login')
def forum(request):
    """
    Display the forum topics and handle the creation of new topics.

    :param request: The HTTP request object.
    :return: Rendered HTML page with the list of topics.
    """
    topics = Topic.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            Topic.objects.create(name=name, createdby=request.user)
            return redirect('forum')
    return render(request, 'forum.html', {'topics': topics})


@login_required(login_url='login')
def topic_detail(request, topic_id):
    """
    Display the details of a specific topic and handle the creation of new posts.

    :param request: The HTTP request object.
    :param topic_id: The ID of the topic to display.
    :return: Rendered HTML page with the topic details and its posts.
    """
    topic = get_object_or_404(Topic, id=topic_id)
    posts = topic.posts.all()
    if request.method == 'POST':
        if 'delete_topic' in request.POST and (topic.createdby == request.user or request.user.has_perm('forum.delete_topic')):
            topic.delete()
            return redirect('forum')
        title=request.POST.get('title')
        content=request.POST.get('content')
        if title and content:
            Post.objects.create(title=title, content=content, author=request.user, topic=topic)
            return redirect('topic_detail', topic_id=topic.id)
    return render(request, 'topic_detail.html', {'topic': topic, 'posts': posts})

@login_required(login_url='login')
def create_topic(request):
    """
    Handle the creation of a new topic.

    :param request: The HTTP request object.
    :return: Redirect to the forum page or render the topic creation page.
    """
    if request.method == 'POST':
        name = request.POST.get('name')
        createdby = request.user
        Topic.objects.create(name=name, createdby=createdby)
        return redirect('forum')
    return render(request, 'create_topic.html')

@login_required(login_url='login')
def post_detail(request, post_id):
    """
    Display the details of a specific post and handle the creation of new comments.

    :param request: The HTTP request object.
    :param post_id: The ID of the post to display.
    :return: Rendered HTML page with the post details and its comments.
    """
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()
    print(request.user.get_all_permissions())
    if request.method == 'POST':
        if 'delete_post' in request.POST and (post.author == request.user or request.user.has_perm('forum.delete_post')):
            post.delete()
            return redirect('forum')
<<<<<<< HEAD
        if 'delete_comment' in request.POST:
            comment_id = request.POST.get('comment_id')
            comment = get_object_or_404(Comment, id=comment_id)

            if comment.author == request.user or request.user.has_perm('forum.delete_comment'):
                comment.delete()

            return redirect('post_detail', post_id=post.id)
        comment= request.POST.get('comment')
=======
        comment = request.POST.get('comment')
>>>>>>> 27f55bb87e699e06b04ccab47ca2037fb1858251
        if comment:
            Comment.objects.create(content=comment, author=request.user, post=post)
            return redirect('post_detail', post_id=post.id)
    return render(request, 'post_detail.html', {'post': post, 'comments': comments})

@login_required(login_url='login')
def create_post(request):
    """
    Handle the creation of a new post.

    :param request: The HTTP request object.
    :return: Redirect to the forum page or render the post creation page.
    """
    topics = Topic.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        topic_id = request.POST.get('topic')
        topic = get_object_or_404(Topic, id=topic_id)
        Post.objects.create(title=title, content=content, author=request.user, topic=topic)
        return redirect('forum')
    return render(request, 'create_post.html', {'topics': topics})

@login_required(login_url='login')
def create_comment(request):
    """
    Handle the creation of a new comment.

    :param request: The HTTP request object.
    :return: Redirect to the post detail page or render the comment creation page.
    """
    posts = Post.objects.all()
    if request.method == 'POST':
        comment = request.POST.get('comment_id')
        post_id = request.POST.get('post')
        post = get_object_or_404(Post, id=post_id)
        Comment.objects.create(content=comment, author=request.user, post_id=post_id)
        return redirect('post_detail', post_id=post.id)
    return render(request, 'create_comment.html', {'posts': posts})
