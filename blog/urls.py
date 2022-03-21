from django.urls import path
from .views import post_list
from .views import post_detail

urlpatterns = [
#   path('', views.post_list, name='post_list'),
    path('list/',post_list,name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', post_detail, name='post_detail'),
]