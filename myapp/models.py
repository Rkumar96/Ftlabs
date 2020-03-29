from django.db import models

class User(models.Model):
	"""user model which holds the user detail's"""
	uid			= models.CharField(max_length=9)
	tz 			= models.CharField(max_length=20)
	real_name   = models.CharField(max_length=20)
	#activity_periods = models.ForeignKey(Activity_Periods, on_delete=models.CASCADE,null=True)

	def __str__(self):
		return self.real_name

	@property
	def activity_periods(self):
		return self.activity_periods_set.all()
	

class Activity_Periods(models.Model):
	"""Activity_Period model which store the start and end time for each users"""
	start_time = models.DateTimeField()
	end_time   = models.DateTimeField()
	user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)

		


