from django.conf.urls import patterns, url, include

from backend import views


urlpatterns = patterns('',
	url(r'^applications$', views.ApplicationList.as_view(), name='application-list'),
	url(r'^applications/(?P<pk>[0-9]+)$', views.ApplicationDetail.as_view(), name='application-detail'),
	
	url(r'^incomes$', views.IncomeList.as_view(), name='income-list'),
	url(r'^incomes/(?P<pk>[0-9]+)$', views.IncomeDetail.as_view(), name='income-detail'),

	url(r'^degree-subjects$', views.DegreeSubjectList.as_view(), name='degree-subject-list'),
	url(r'^degree-subjects/(?P<pk>[0-9]+)$', views.DegreeSubjectDetail.as_view(), name='degree-subject-detail'),

	url(r'^postgraduate-subjects$', views.PostgraduateSubjectList.as_view(), name='postgraduate-subject-list'),
	url(r'^postgraduate-subjects/(?P<pk>[0-9]+)$', views.PostgraduateSubjectDetail.as_view(), name='postgraduate-subject-detail'),

	url(r'^degree-types$', views.DegreeTypeList.as_view(), name='degree-type-list'),
	url(r'^degree-types/(?P<pk>[0-9]+)$', views.DegreeTypeDetail.as_view(), name='degree-type-detail'),
)