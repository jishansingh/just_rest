from django.shortcuts import render
from .models import NewUser
from .serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from rest_framework.decorators import APIView,api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
# Create your views here.
class ListUser(APIView):
    def get(self,request):
        user=NewUser.objects.all()
        serializer=UserSerializer(user,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializers.errors,status=401)

class DetailView(APIView):
    def get_object(self,id):
        user=get_object_or_404(NewUser,id=id)
        return user
    def get(self,request,id):
        serializer=UserSerializer(self.get_object(id))
        return Response(serializer.data)
    def put(self,request,id):
        user=get_object_or_404(NewUser,id=id)
        serializer=UserSerializer(self.get_object(id),data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=401)
    def delete(self,request,id):
        user=self.get_object(id)
        user.delete()
        return Response(status=204)
kjjjkj
