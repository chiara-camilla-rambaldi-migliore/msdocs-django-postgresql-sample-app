from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

class User(models.Model):
    name = models.CharField(max_length=200)

class Transform(models.Model):
    transform = models.JSONField()
    userId = models.ForeignKey(User, on_delete=models.CASCADE)

class Image(models.Model):
    images = models.JSONField()
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    transformId = models.ForeignKey(Transform, on_delete=models.CASCADE)