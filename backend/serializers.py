from backend.models import *

from rest_framework import serializers

class ApplicationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Application




class IncomeSerializer(serializers.ModelSerializer):
	string = serializers.SerializerMethodField('_string')

	class Meta:
		model = Income

	def _string(self, obj):
		return obj.toString()


class DegreeSubjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = DegreeSubject


		

class PostgraduateSubjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = PostgraduateSubject




class DegreeTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model = DegreeType