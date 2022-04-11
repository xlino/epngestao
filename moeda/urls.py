from django.urls import path
from .import views


urlpatterns = [
    path('teste/', views.teste, name='teste'),
    path('listamoeda/', views.listamoeda, name='listamoeda'),
]

