from django.db import models

# Create your models here.

class Books(models.Model):
	title = models.CharField(max_length=150)
	autor = models.CharField(max_length=100)
	read = models.CharField(max_length=3)
	