from django.conf.urls import patterns, include, url
from django.conf import settings
from articles.views import *
# from mptt_urls import url_mptt
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
mptt_urls_articles_settings = {
    'node': {
        'model': 'articles.models.Category',
        'view': 'articles.views.category',
        'slug_field': 'CategorySlug',
    },
    'leaf': {
        'model': 'articles.models.Article',
        'template': 'article-video-hybrid.html',
        'slug_field': 'Slug',
    }
}
urlpatterns = []
if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))

urlpatterns += patterns('articles.views',
	#url(r'^$', landing),
	#url(r'^about/$', about_page),
	url(r'^(?P<category>[a-z-0-9]+)/$', get_category),
	url(r'^(?P<category>[a-z-0-9]+)/(?P<article_slug>[a-z-/0-9]+)/$', get_article),
	# url_mptt(r'^(?P<url>.*)', name='article', settings=mptt_urls_articles_settings),
)
