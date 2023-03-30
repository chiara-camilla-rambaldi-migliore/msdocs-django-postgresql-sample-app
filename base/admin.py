from django.contrib import admin
from .models import Item, User, Transform, Image

# Register your models here.

admin.site.register(Item)
admin.site.register(User)
admin.site.register(Transform)
admin.site.register(Image)