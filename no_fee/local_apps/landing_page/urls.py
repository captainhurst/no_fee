from django.conf.urls import patterns, include, url
from landing_page.views import *

urlpatterns = patterns('landing_page.views',
	url(r'^$', landing),
	# url(r'^ajax/email_capture$', email_capture),

	#url(r'x/$', directory),
	#url(r'^(?P<category>[a-z]+)/(?P<office>[a-z-0-9]+)/$', directory),
)
