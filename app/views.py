from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def userlogin(request):
    return render(request, 'login.html')

def userregister(request):
    return render(request, 'register.html')

def userlogout(request):
    return render(request, 'logout.html')