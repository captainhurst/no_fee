# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.template import RequestContext, loader
from django.contrib import auth
from django.conf import settings as conf_settings
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
# from django.contrib.sites.models import Site
# from django.contrib.sites.models import get_current_site
from django.contrib.contenttypes.models import ContentType
# from django.contrib.contenttypes import generic
# from django.db import IntegrityError
# from django.core.cache import cache
from django.db.models import Q
from urlparse import urlparse
from datetime import datetime
from itertools import chain
from mptt.utils import drilldown_tree_for_node
from django.db.models.query import EmptyQuerySet
from articles.models import ArticleMedia, Article, FeaturedArticle, Category
from models import FAQ
from contact.forms import ContactForm
import pprint

# from landing_page.forms import EmailCaptureForm



def faq_page(request):
	articles = Article.objects.all().order_by('-PublishTime')
	articles.featured = list(articles.filter(isFeatured=True).order_by('-PublishTime'))[0:6]
	faqs = FAQ.objects.all().order_by('Rank')
	context = {'faqs': faqs, 'articles': articles }
	return render(request, 'faqs.html', context)	








			

