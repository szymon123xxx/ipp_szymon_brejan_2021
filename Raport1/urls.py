from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="films-home"),
    path('about/', views.about, name="films-about"),
    path('index/', views.index, name='index-films'),
]
