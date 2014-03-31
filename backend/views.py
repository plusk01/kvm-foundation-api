from backend.models import *
from backend.serializers import *

from rest_framework import generics




class ApplicationList(generics.ListCreateAPIView):
	queryset = Application.objects.all()
	serializer_class = ApplicationSerializer

class ApplicationDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Application.objects.all()
	serializer_class = ApplicationSerializer




class IncomeList(generics.ListCreateAPIView):
	queryset = Income.objects.all()
	serializer_class = IncomeSerializer

class IncomeDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Income.objects.all()
	serializer_class = IncomeSerializer




class DegreeSubjectList(generics.ListCreateAPIView):
	queryset = DegreeSubject.objects.all()
	serializer_class = DegreeSubjectSerializer

class DegreeSubjectDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = DegreeSubject.objects.all()
	serializer_class = DegreeSubjectSerializer




class PostgraduateSubjectList(generics.ListCreateAPIView):
	queryset = PostgraduateSubject.objects.all()
	serializer_class = PostgraduateSubjectSerializer

class PostgraduateSubjectDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = PostgraduateSubject.objects.all()
	serializer_class = PostgraduateSubjectSerializer