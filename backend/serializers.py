from backend.models import *

from rest_framework import serializers

class ApplicationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Application




class IncomeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Income




class DegreeSubjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = DegreeSubject


		

class PostgraduateSubjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = PostgraduateSubject