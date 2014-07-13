from django.conf.urls import patterns, include, url
from auto_content.views import *

urlpatterns = patterns('articles.views',
	#url(r'^$', landing),
	#url(r'^about/$', about_page),
	url(r'^t/$', get_links),
	#url(r'^s/$', scrape_links),
	url(r'^k/$', keywords),	
	url(r'^h/$', handles),
	url(r'^gs/$', get_stories),
)
