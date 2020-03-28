from django.db import models

class User(models.Model):
	"""docstring for User"""
	uid			= models.CharField(max_length=9)
	tz 			= models.CharField(max_length=20)
	real_name   = models.CharField(max_length=20)

	def __str__(self):
		return self.real_name

class Activity_Periods(models.Model):
	"""docstring for Activity_Period"""
	start_time = models.DateTimeField()
	end_time   = models.DateTimeField()
	user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)

		


