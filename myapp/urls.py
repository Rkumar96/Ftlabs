from django.urls import path
from . import views

 '''
	mapped three url api endpoints
	1: api overview --whic displays how many endpoints are there
	2: user-list --for displaying the all user entry
	3: user-detail/<str:pk>/  --for displaying the perticular user by pasing pk id in the url
 '''
urlpatterns = [
    path('', views.index, name='api-overview'),
    path('user-list/', views.userList, name='user-list'),
    path('user-detail/<str:pk>/', views.userDetail, name='user-detail'),
]