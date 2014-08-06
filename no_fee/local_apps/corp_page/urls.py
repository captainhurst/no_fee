from django.conf.urls import patterns, include, url
from django.conf import settings
from corp_page.views import *
# from mptt_urls import url_mptt
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
urlpatterns = []
if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))

urlpatterns += patterns('corp_page.views',
	#url(r'^$', landing),
	url(r'^company/(?P<corp_slug>[a-z-0-9]+)/$', corp_page),
	# url_mptt(r'^(?P<url>.*)', name='article', settings=mptt_urls_articles_settings),
)
