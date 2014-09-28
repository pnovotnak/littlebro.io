import random

from django.views.generic import TemplateView
from django.contrib import admin
from django.conf.urls import patterns, include, url

from littlebro import views
from recaptcha.forms import CaptchaLoginForm

handler404 = TemplateView.as_view(template_name="404.html")

admin.site.login_form = CaptchaLoginForm
admin.site.login_template = 'admin/grappelli-captcha-login.html'
admin.site.site_header = (
    'LittleBro.io Administration'
)

super_admin = patterns('',
    (r'^', include('smuggler.urls')),  # before admin url patterns!
    url(r'^', include(admin.site.urls)),
)

urlpatterns = patterns('',
    (r'^grappelli/', include('grappelli.urls')), # grappelli URLS

    (r'^admin/', include(super_admin)),

    (r'^ckeditor/', include('ckeditor.urls')),
)

urlpatterns += patterns('django.contrib.flatpages.views',
    (r'^(?P<url>.*/?)$', 'flatpage'),
)
