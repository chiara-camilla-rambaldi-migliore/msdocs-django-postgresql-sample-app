from rest_framework import serializers
from base.models import Item, User, Transform, ImageCollection

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
        

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class TransformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transform
        fields = '__all__'

class ImageCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageCollection
        fields = '__all__'