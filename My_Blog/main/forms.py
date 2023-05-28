from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import UserManager
from django import forms
from .models import Article, Comment

class AddBlogForm(forms.ModelForm):
    title = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'write down slug', 'class':'form-control'}))
    content = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'write down slug', 'class':'form-control'}))
    slug = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'write down slug', 'class':'form-control'}))
    # post_image = forms.ImageField(upload_to='uploads/', default="default_post_image.jpg")

    class Meta:
        model = Article
        fields = ['title', 'slug', 'content', 'post_image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']