from django.db import models

# Create your models here.

class Application(models.Model):
	MALE = 'M'
	FEMALE = 'F'
	GENDER_CHOICES = (
		(MALE, 'Male'),
		(FEMALE, 'Female'),
	)

	# Personal Information
	first_name = models.CharField(max_length=75)
	last_name = models.CharField(max_length=75)
	birthday = models.DateField()
	gender = models.CharField(choices=GENDER_CHOICES)
	email = models.CharField(max_length=75)
	mobile = models.CharField(max_length=20)
	father = models.CharField(max_length=150)
	present_address = models.CharField(max_length=255)
	permanent_address = models.CharField(max_length=255)

	# Financial Information
	parents_income = models.ForeignKey('Income')
	mother_job = models.CharField(max_length=100)
	father_job = models.CharField(max_length=100)
	position = models.ManyToMany('Position')