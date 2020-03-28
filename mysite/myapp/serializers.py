from rest_framework import serializers
from .models import User,Activity_Periods

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'


class ASerializer(serializers.ModelSerializer):
	class Meta:
		model = Activity_Periods
		fields = '__all__'
