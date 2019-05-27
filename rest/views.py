from django.shortcuts import render
from .models import NewUser
from .serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from django.shortcuts import get_object_or_404
# Create your views here.
@csrf_exempt
def ListUser(request):
    if request.method=='GET':
        user=NewUser.objects.all()
        serializer=UserSerializer(user,many=True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method=='POST':
        data=JSONParser(request)
        serialize=UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,staus=201)
        else:
            return JsonResponse(serializer.errors,status=400)

def DetailView(request,id):
    user=get_object_or_404(NewUser,id=id)
    if request.method=='GET':
        serializer=UserSerializer(user)
        return JsonResponse(serializer.data)
    elif request.method=='PUT':
        data=JsonParser(request)
        serializer=UserSerializer(user,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            return JsonResoponse(serializers.errors,status=400)


