import random

from django.contrib import admin
from django.conf.urls import patterns, include, url

from littlebro import views

admin.autodiscover()
admin.site.site_header = 'LittleBro.io Administration'
admin.site.index_title = random.choice((
    'Who watches the watchmen?',
    'With great power comes great responsibility'
))


police_officer_patterns = patterns('',
    url(r'^$', views.PoliceOfficerList.as_view()),
    url(r'^add/?$', views.PoliceOfficerCreate.as_view()),
    url(r'^(?P<pk>[0-9]+)/?$', views.PoliceOfficerDetail.as_view()),
)

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    # Model URLs
    url(r'^police-officers/?', include(police_officer_patterns)),

    (r'^ckeditor/', include('ckeditor.urls')),
)

urlpatterns += patterns('django.contrib.flatpages.views',
    (r'^(?P<url>.*/?)$', 'flatpage'),
)
