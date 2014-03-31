from django.db import models

# Create your models here.

class Application(models.Model):
	MALE = 'M'
	FEMALE = 'F'
	GENDER_CHOICES = (
		(MALE, 'Male'),
		(FEMALE, 'Female'),
	)

	EMPLOYED = 'E'
	UNEMPLOYED = 'U'
	STUDENT = 'S'
	POSITION_CHOICES = (
		(EMPLOYED, 'Employed'),
		(UNEMPLOYED, 'Unemployed'),
		(STUDENT, 'Student'),
	)

	ENGLISH = 'E'
	TELUGU = 'T'
	MEDIUM_CHOICES = (
		(ENGLISH, 'English'),
		(TELUGU, 'Telugu'),
	)

	DIVISION_1 = 'D1'
	DIVISION_2 = 'D2'
	DIVISION_3 = 'D3'
	DIVISION_4 = 'D4'
	DIVISION_CHOICES = (
		(DIVISION_1, '1st'),
		(DIVISION_2, '2nd'),
		(DIVISION_3, '3rd'),
		(DIVISION_4, '4th'),
	)

	YEAR_1 = 'Y1'
	YEAR_2 = 'Y2'
	YEAR_3 = 'Y3'
	YEAR_4 = 'Y4'
	YEAR_5 = 'Y5'
	YEAR_CHOICES = (
		(YEAR_1, '1st Year'),
		(YEAR_2, '2nd Year'),
		(YEAR_3, '3rd Year'),
		(YEAR_4, '4th Year'),
		(YEAR_5, '5th Year'),
	)

	# Personal Information
	first_name = models.CharField(max_length=75)
	last_name = models.CharField(max_length=75)
	birthday = models.DateField()
	gender = models.CharField(choices=GENDER_CHOICES, max_length=1)
	email = models.CharField(max_length=75)
	mobile = models.CharField(max_length=20)
	father = models.CharField(max_length=150)
	present_address = models.CharField(max_length=255)
	permanent_address = models.CharField(max_length=255)

	# Financial Information
	parents_income = models.ForeignKey('Income', related_name='+')
	mother_job = models.CharField(max_length=100)
	father_job = models.CharField(max_length=100)
	position = models.CharField(choices=POSITION_CHOICES, max_length=1)
	occupation = models.CharField(max_length=100)
	income = models.ForeignKey('Income', related_name='+')

	# Educational Information
	# Primary
	primary_school = models.CharField(max_length=100)
	primary_medium = models.CharField(choices=MEDIUM_CHOICES, max_length=1)
	primary_marks = models.DecimalField(max_digits=4, decimal_places=2)
	primary_division = models.CharField(choices=DIVISION_CHOICES, max_length=2)
	primary_passing = models.IntegerField(max_length=4)

	# Intermediate
	intermediate_subjects = models.CharField(max_length=100)
	intermediate_college = models.CharField(max_length=100)
	intermediate_medium = models.CharField(choices=MEDIUM_CHOICES, max_length=1)
	intermediate_marks = models.DecimalField(max_digits=4, decimal_places=2)
	intermediate_division = models.CharField(choices=DIVISION_CHOICES, max_length=2)
	intermediate_passing = models.IntegerField(max_length=4)

	# Degree
	degree_subject = models.ForeignKey('DegreeSubject')
	degree_college = models.CharField(max_length=100)
	degree_medium = models.CharField(choices=MEDIUM_CHOICES, max_length=1)
	degree_marks = models.DecimalField(max_digits=4, decimal_places=2)
	degree_division = models.CharField(choices=DIVISION_CHOICES, max_length=2)
	degree_passing = models.IntegerField(max_length=4)
	degree_current_year = models.CharField(choices=YEAR_CHOICES, max_length=2)

	# Postgraduate Degree
	post_subject = models.ForeignKey('PostgraduateSubject')
	post_university = models.CharField(max_length=100)
	post_medium = models.CharField(choices=MEDIUM_CHOICES, max_length=1)
	post_marks = models.DecimalField(max_digits=4, decimal_places=2)
	post_division = models.CharField(choices=DIVISION_CHOICES, max_length=2)
	post_passing = models.IntegerField(max_length=4)
	post_current_year = models.CharField(choices=YEAR_CHOICES, max_length=2)

	academic_distinction = models.TextField()

	essay = models.TextField()

	def __unicode__(self):
		print "%s %s" % (self.first_name, self.last_name)

class Income(models.Model):
	lower_bound = models.IntegerField()
	upper_bound = models.IntegerField()

	def __unicode__(self):
		print "Income: " + str(self.lower_bound) + " to " + str(self.upper_bound)

class DegreeSubject(models.Model):
	name = models.CharField(max_length=30)

	def __unicode__(self):
		print "Degree Subject: " + str(self.name)

class PostgraduateSubject(models.Model):
	name = models.CharField(max_length=30)

	def __unicode__(self):
		print "Postgraduate Subject: " + str(self.name)