from rest_framework import serializers
from .models import User,Activity_Periods


class ASerializer(serializers.ModelSerializer):
	class Meta:
		model = Activity_Periods
		fields = [
			"start_time",
			"end_time",
		]
		

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


