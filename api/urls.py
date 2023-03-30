from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('add/', views.addItem),
    path('transforms', views.getTransforms),
    path('transforms?user=<int>', views.getTransforms),
    path('images', views.getImages),
    #path('images/?user=<int>&transform=<int>', views.getImages),
    path('images?user=<int>', views.getImages),
    path('users', views.getUsers),
    path('users?id=<int>', views.getUsers),
    path('addUser/', views.addUser),
    path('addTransform/', views.addTransform),
]