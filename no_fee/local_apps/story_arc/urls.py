# from django.conf.urls import patterns, include, url
# from django.conf import settings
# from story_arc.views import *
# # Uncomment the next two lines to enable the admin:
# # from django.contrib import admin
# # admin.autodiscover()
# urlpatterns = []
# if settings.DEBUG:
#     # static files (images, css, javascript, etc.)
#     urlpatterns += patterns('',
#         (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
#         'document_root': settings.MEDIA_ROOT}))

# urlpatterns += patterns('story_arc.views',
# 	url(r'^sa/$', story_arc),
# 	url(r'^story/(?P<category>[a-z-0-9]+)/(?P<story_slug>[a-z-0-9]+)$', get_story_arc),
# )
