from django.shortcuts import render
from .models import NewUser
from .serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
# Create your views here.
@api_view(['GET', 'PUT', 'DELETE'])
def ListUser(request):
    if request.method=='GET':
        user=NewUser.objects.all()
        serializer=UserSerializer(user,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serialize=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,staus=201)
        else:
            return Response(serializers.errors,status=400)
@api_view(['GET', 'PUT', 'DELETE'])
def DetailView(request,id):
    user=get_object_or_404(NewUser,id=id)
    if request.method=='GET':
        serializer=UserSerializer(user)
        return Response(serializer.data)
    elif request.method=='PUT':
        serializer=UserSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializers.errors,status=400)


