from django.conf.urls import patterns, include, url
from contact.views import *
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('contact.views',
	url(r'^contact/$', contact),

)
