from django.conf.urls import patterns, include, url

from littlebro import views

from base import *

judge_patterns = patterns('',
    url(r'^$', views.JudgeList.as_view()),
    url(r'^add/?$', views.JudgeCreate.as_view()),
    url(r'^(?P<pk>[0-9]+)/?$', views.JudgeDetail.as_view()),
)

urlpatterns += patterns('',
    # Model URLs
    url(r'^judges/?', include(police_officer_patterns)),
)