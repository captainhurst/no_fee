from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse
import datetime
from random import randrange
from django.core.urlresolvers import reverse
from articles.models import Category, Article
from corp_page.models import CorpPage
from contact.views import contact
from landing_page.views import landing

class ArticleSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8
    
    def items(self):
        return Article.objects.all()
    
    def lastmod(self, obj):
        return obj.PublishTime
    
    def location(self, obj):
        return '%s%s/' % (obj.ParentCategory.get_absolute_url(), obj.Slug)
        
class CorpPageSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return CorpPage.objects.all()

    def lastmod(self, obj):
        return obj.PublishTime

    def location(self, obj):
        return '/company/%s/' % obj.PageSlug

class StaticViewSitemap(Sitemap):
    priority = 0.9
    changefreq = 'daily'

    def items(self):
        return [landing, contact]

    def location(self, item):
        return reverse(item)
