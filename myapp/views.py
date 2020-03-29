from django.shortcuts import render
from django.http import JsonResponse
#imports for the rest api
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer,ASerializer
#importing two models from models module
from .models import User,Activity_Periods

#this function returns the JSON object of api overview
@api_view(['GET'])
def index(request):

	api_urls = {
		'List':'/user-list',
		'Detail View':'/user-detail/<str:pk>'
	}

	return Response(api_urls)
#this function returns the JSON object of all user
@api_view(['GET'])
def userList(request):
	users = User.objects.all()
	serializer = UserSerializer(users, many=True)
	return Response(serializer.data)

#this function take's second parameter "pk" which is primary key of user table returns the perticular user's JSON object
@api_view(['GET'])
def userDetail(request,pk):
	users = User.objects.get(id=pk)
	serializer = UserSerializer(users, many=False)
	return Response(serializer.data)