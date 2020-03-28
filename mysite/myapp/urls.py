from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='api-overview'),
    path('user-list/', views.userList, name='user-list'),
    path('a-list/', views.aList, name='a-list'),
]