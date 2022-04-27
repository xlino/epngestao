from django.shortcuts import render, redirect
from django.contrib.auth.decorators  import  login_required
from django.contrib.auth import logout

# Create your views here.

def teste(request):
    return render(request, 'home/teste.html')


def home(request):
    return render(request, 'home/home.html')

def mylogout(request):
    logout(request)
    return render(request, 'home/home.html')

#@login_required
#def dashboard(request):

 #   return render(request, 'projetos/dashboard.html'
 #                 )
