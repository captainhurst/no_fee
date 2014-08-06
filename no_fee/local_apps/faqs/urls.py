from django.conf.urls import patterns, include, url
from django.conf import settings
from faqs.views import *
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

urlpatterns += patterns('faqs.views',
	#url(r'^$', landing),
	url(r'^faqs/$', faq_page),
	# url_mptt(r'^(?P<url>.*)', name='article', settings=mptt_urls_articles_settings),
)
