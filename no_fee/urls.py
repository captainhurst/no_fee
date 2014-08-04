from django.conf.urls import patterns, include, url
import landing_page, articles
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rbh_me.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('landing_page.urls')),
    # url(r'', include('contact.urls')),
    url(r'', include('articles.urls')),


)
