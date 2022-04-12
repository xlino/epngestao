from django.urls import path
from . import views

urlpatterns = [
    path('teste/', views.teste, name='teste'),
    path('', views.home, name='home'),
    path('logout', views.logout, name='logout'),
]