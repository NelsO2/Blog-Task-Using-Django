from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from main.models import Article
from django.core.paginator import Paginator
# Create your views here.

def home(request):
    articles = Article.objects.all()
    paginator = Paginator(articles, 2)
    pageNumber = request.GET.get('page')
    homeData = paginator.get_page(pageNumber)
    totalPage = homeData.paginator.num_pages
    return render(request, 'home.html', {'homeData':homeData, 'totalPage':totalPage, 'listofPages':[n+1 for n in range(totalPage)]})

def signup_user(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "signup successful")

    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form':form})

  
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # authentication
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You are logged in")
            return redirect("home")
        else:
            messages.error(request, "please try again")
            return redirect('login_user')
    else:
        return render(request, 'login_user.html', {})
    

def logout_user(request):
    logout(request)
    messages.success(request, "You have logged out")
    return redirect('login_user')