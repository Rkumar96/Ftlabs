from rest_framework import serializers
from .models import User,Activity_Periods

#this Serializer class is responsible for converting the data of Activity_Periods models into JSON obj
class ASerializer(serializers.ModelSerializer):
	class Meta:
		model = Activity_Periods
		fields = [
			"start_time",
			"end_time",
		]
		
#this Serializer class is responsible for converting the data of user models into JSON obj
class UserSerializer(serializers.ModelSerializer):
	activity_periods = ASerializer(many=True)

	class Meta:
		model = User
		fields = [
			"uid",
			"tz",
			"real_name",
			"activity_periods",
		]
		depth = 2


