from django.shortcuts import render, get_object_or_404
from .models import Article
from django.contrib.auth.decorators import login_required

# Create your views here.

def details(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'details.html', {'article':article})
