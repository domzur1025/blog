from django import forms
from .models import Comment, Post, Category

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('category', 'title', 'content', 'status')
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title',)