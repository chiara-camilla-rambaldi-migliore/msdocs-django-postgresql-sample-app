from django.contrib import admin
from .models import Item, User, Transform, ImageCollection

# Register your models here.

admin.site.register(Item)
admin.site.register(User)
admin.site.register(Transform)
admin.site.register(ImageCollection)