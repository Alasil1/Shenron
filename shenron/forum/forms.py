# forms.py
from django import forms
from .models import Post, Comment, Topic

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content','topic']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
# forms.py

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['name']