from django.conf.urls import patterns, include, url

from littlebro import views

from base import *

police_officer_patterns = patterns('',
    url(r'^$', views.PoliceOfficerList.as_view()),
    url(r'^add/?$', views.PoliceOfficerCreate.as_view()),
    url(r'^(?P<pk>[0-9]+)/?$', views.PoliceOfficerDetail.as_view()),
)

urlpatterns += patterns('',
    # Model URLs
    url(r'^police/?', include(police_officer_patterns)),
)