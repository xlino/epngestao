from django.shortcuts import render, redirect
from django.contrib.auth import logout

# Create your views here.
def teste(request):
    return render(request, 'home/teste.html')

def home(request):
    return render(request, 'home/home.html')

def logout(request):
    logout(request)
    return redirect ('home')

