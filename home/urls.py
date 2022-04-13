from django.urls import path
from .views import home, mylogout, teste, dashboard

urlpatterns = [
    path('teste/', teste, name='teste'),
    path('', home, name='home'),
    path('logout/', mylogout, name='logout'),
    path('projetos/dashboard/', dashboard, name='dashboard'),
]