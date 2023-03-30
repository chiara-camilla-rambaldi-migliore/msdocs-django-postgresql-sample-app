from rest_framework.response import Response
from rest_framework.request import HttpRequest
from rest_framework.decorators import api_view
from base.models import Item, Transform, User, Image
from .serializers import ItemSerializer, TransformSerializer, UserSerializer, ImageSerializer

@api_view(['GET'])
def getData(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getTransforms(request: HttpRequest):
    user = request.GET.get('user', '')
    if user == '':
        items = Transform.objects.all()
    else:
        items = Transform.objects.get(userId=user)
    serializer = TransformSerializer(items, many=hasattr(items, '__iter__'))
    return Response(serializer.data)

@api_view(['GET'])
def getImages(request: HttpRequest):
    user = request.GET.get('user', '')
    transform = request.GET.get('transform', '')
    if user == '' and transform == '':
        items = Image.objects.all()
    elif transform == '':
        items = Image.objects.get(userId=user)
    else:
        items = Image.objects.get(userId=user, transformId=transform)
    serializer = ImageSerializer(items, many=hasattr(items, '__iter__'))
    return Response(serializer.data)

@api_view(['GET'])
def getUsers(request: HttpRequest):
    id = request.GET.get('id', '')
    if id == '':
        items = User.objects.all()
    else:
        items = User.objects.get(id=id)
    serializer = UserSerializer(items, many=hasattr(items, '__iter__'))
    return Response(serializer.data)

@api_view(['POST'])
def addItem(request: HttpRequest):
    serializer = ItemSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def addUser(request: HttpRequest):
    serializer = UserSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def addTransform(request: HttpRequest):
    serializer = TransformSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
