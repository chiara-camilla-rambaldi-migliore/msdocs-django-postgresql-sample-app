from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('add/', views.addItem),
    path('transforms/', views.getTransforms),
    path('images/', views.getImages),
    path('users/', views.getUsers),
    path('addUser/', views.addUser),
    path('addTransform/', views.addTransform),
]