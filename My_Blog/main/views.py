from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import AddBlogForm, CommentForm
from django.db.models import F
# Create your views here.
@login_required(login_url='login_user')
def details(request, slug):
    article = get_object_or_404(Article, slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            form = CommentForm()
    else:
        form = CommentForm()
    comments = article.comments.annotate(reversed_id=F('id')*-1).order_by('reversed_id')
    return render(request, 'details.html', {'article':article, 'form':form, 'comments':comments})


@login_required(login_url='login_user')
def addBlogs(request):
    form = AddBlogForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            add_blog = form.save(commit=False)
            add_blog.post_image = form.cleaned_data['post_image']
            add_blog.save()
            messages.success(request, "Blog added successfully")
            return redirect('home')
    return render(request, 'addBlogs.html', {'form':form})
