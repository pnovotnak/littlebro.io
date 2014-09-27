from django.conf.urls import patterns, include, url

from littlebro import views

from base import *

legislator_patterns = patterns('',
    url(r'^$', views.LegislatorList.as_view()),
    url(r'^add/?$', views.LegislatorCreate.as_view()),
    url(r'^(?P<pk>[0-9]+)/?$', views.LegislatorDetail.as_view()),
)

urlpatterns += patterns('',
    # Model URLs
    url(r'^legislators/?', include(legislator_patterns)),
)