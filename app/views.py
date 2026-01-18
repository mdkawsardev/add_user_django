from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import LoginUser
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    return render(request, 'index.html')

def userlogin(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, f"Welcome {username}")
            context = {
                'username': 'imrankhan'
            }
            return redirect('home')
        else:
            messages.info(request, 'Invalid Credintial!')
            return render(request, 'login.html')
    return render(request, 'login.html')

def userregister(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists!')
                return redirect('/register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists!')
                return redirect('/register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, 'New user added successfully!')
                return redirect('/login')
        else: 
            messages.info(request, 'Password did\'t match!')
            return redirect('/register')
    return render(request, 'register.html')

def userlogout(request):
    logout(request)
    return redirect('userlogin')