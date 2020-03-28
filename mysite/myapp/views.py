from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer,ASerializer

from .models import User,Activity_Periods
# Create your views here.


@api_view(['GET', 'POST'])
def index(request):

	api_urls = {
		'List':'/user-list',
		'Detail View':'/user-detail/<str:pk>'
	}

	return Response(api_urls)

@api_view(['GET', 'POST'])
def userList(request):
	users = User.objects.all()
	serializer = UserSerializer(users, many=True)
	return Response(serializer.data)

@api_view(['GET', 'POST'])
def aList(request):
	users = Activity_Periods.objects.all()
	serializer = ASerializer(users, many=True)
	return Response(serializer.data)