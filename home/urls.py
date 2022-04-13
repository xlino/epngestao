from django.urls import path
from .views import home, mylogout, teste

urlpatterns = [
    path('teste/', teste, name='teste'),
    path('', home, name='home'),
    path('logout/', mylogout, name='logout'),
]