from django.db import models

# Create your models here.
class BankDetail(models.Model):
	ifsc = models.CharField(max_length=100)
	bank_id = models.CharField(max_length=200)
	branch = models.CharField(max_length=200)
	address = models.TextField()
	city = models.CharField(max_length=100)
	district = models.CharField(max_length=100)
	state = models.CharField(max_length=100)