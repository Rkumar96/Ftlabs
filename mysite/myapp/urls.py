from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='api-overview'),
    path('user-list/', views.userList, name='user-list'),
    path('user-detail/<str:pk>/', views.userDetail, name='user-detail'),
]