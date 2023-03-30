from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('add/', views.addItem),
    path('transforms', views.getTransforms),
    path('transforms?user=<int>', views.getTransforms),
    path('imageCollections', views.getImageCollections),
    #path('images/?user=<int>&transform=<int>', views.getImages),
    path('imageCollections?user=<int>', views.getImageCollections),
    path('users', views.getUsers),
    path('users?id=<int>', views.getUsers),
    path('addUser/', views.addUser),
    path('addTransform/', views.addTransform),
    path('addImageCollection/', views.addImageCollection),
]