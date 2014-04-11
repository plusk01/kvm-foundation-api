from django.db import models

# Create your models here.

class Application(models.Model):
	MALE = 'M'
	FEMALE = 'F'
	GENDER_CHOICES = (
		(MALE, 'Male'),
		(FEMALE, 'Female'),
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
	permanent_address = models.CharField(max_length=255, null=True, blank=True)

	# Financial Information
	parents_income = models.ForeignKey('Income', related_name='+')
	mother_job = models.CharField(max_length=100, null=True, blank=True)
	father_job = models.CharField(max_length=100, null=True, blank=True)
	# is_employed = models.NullBooleanField()
	# is_looking = models.NullBooleanField()
	# is_student = models.NullBooleanField()
	occupation = models.CharField(max_length=100, null=True, blank=True)
	income = models.ForeignKey('Income', related_name='+', null=True, blank=True)

	# # Educational Information
	# # Primary
	# primary_school = models.CharField(max_length=100, null=True, blank=True)
	# primary_medium = models.CharField(choices=MEDIUM_CHOICES, max_length=1, null=True, blank=True)
	# primary_marks = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
	# primary_division = models.CharField(choices=DIVISION_CHOICES, max_length=2, null=True, blank=True)
	# primary_passing = models.IntegerField(max_length=4, null=True, blank=True)

	# # Intermediate
	# intermediate_subjects = models.CharField(max_length=100, null=True, blank=True)
	# intermediate_college = models.CharField(max_length=100, null=True, blank=True)
	# intermediate_medium = models.CharField(choices=MEDIUM_CHOICES, max_length=1, null=True, blank=True)
	# intermediate_marks = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
	# intermediate_division = models.CharField(choices=DIVISION_CHOICES, max_length=2, null=True, blank=True)
	# intermediate_passing = models.IntegerField(max_length=4, null=True, blank=True)

	# # Degree
	# degree_subject = models.ForeignKey('DegreeSubject', null=True, blank=True)
	# degree_college = models.CharField(max_length=100, null=True, blank=True)
	# degree_medium = models.CharField(choices=MEDIUM_CHOICES, max_length=1, null=True, blank=True)
	# degree_marks = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
	# degree_division = models.CharField(choices=DIVISION_CHOICES, max_length=2, null=True, blank=True)
	# degree_passing = models.IntegerField(max_length=4, null=True, blank=True)
	# degree_current_year = models.CharField(choices=YEAR_CHOICES, max_length=2, null=True, blank=True)

	# # Postgraduate Degree
	# post_subject = models.ForeignKey('PostgraduateSubject', null=True, blank=True)
	# post_university = models.CharField(max_length=100, null=True, blank=True)
	# post_medium = models.CharField(choices=MEDIUM_CHOICES, max_length=1, null=True, blank=True)
	# post_marks = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
	# post_division = models.CharField(choices=DIVISION_CHOICES, max_length=2, null=True, blank=True)
	# post_passing = models.IntegerField(max_length=4, null=True, blank=True)
	# post_current_year = models.CharField(choices=YEAR_CHOICES, max_length=2, null=True, blank=True)

	# academic_distinction = models.TextField(null=True, blank=True)

	## Added to make Application simpler
	current_degree = models.ForeignKey('DegreeType', related_name='+')
	current_degree_user = models.CharField(max_length=255, null=True, blank=True)
	current_year = models.CharField(choices=YEAR_CHOICES, max_length=2, null=True, blank=True)
	current_subjects = models.CharField(max_length=255, null=True, blank=True)
	institution_name = models.CharField(max_length=255, null=True, blank=True)

	essay = models.TextField()

	def __unicode__(self):
		return "%s %s" % (self.first_name, self.last_name)

class Income(models.Model):
	lower_bound = models.IntegerField()
	upper_bound = models.IntegerField()

	def __unicode__(self):
		return "Income: " + self.toString()

	def toString(self):
		import locale

		try:
			locale.setlocale(locale.LC_ALL, 'en_IN.utf8')
		except:
			locale.setlocale(locale.LC_ALL, '')

		low = locale.format("%.2f", self.lower_bound, grouping=True)
		high = locale.format("%.2f", self.upper_bound, grouping=True)

		return "%s to %s rupees" % (low, high)


class DegreeSubject(models.Model):
	name = models.CharField(max_length=30)

	def __unicode__(self):
		return "Degree Subject: " + str(self.name)

class PostgraduateSubject(models.Model):
	name = models.CharField(max_length=30)

	def __unicode__(self):
		return "Postgraduate Subject: " + str(self.name)

class DegreeType(models.Model):
	name = models.CharField(max_length=50)

	def __unicode_(self):
		return "Type: " + str(self.name)