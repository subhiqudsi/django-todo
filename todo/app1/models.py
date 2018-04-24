from django.db import models

# Create your models here.
class Todo(models.Model):
	sess = models.CharField(max_length=64)
	text = models.CharField(max_length=40)
	complete = models.BooleanField(default=False)

	def __str__(self):
		return self.text