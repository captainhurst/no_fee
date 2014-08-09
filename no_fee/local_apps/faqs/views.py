# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.template import RequestContext, loader
from django.contrib import auth
from django.conf import settings as conf_settings
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from urlparse import urlparse
from datetime import datetime
from itertools import chain
from mptt.utils import drilldown_tree_for_node
from django.db.models.query import EmptyQuerySet
from articles.models import ArticleMedia, Article, FeaturedArticle, Category
from landing_page.models import DefaultSocialImage
from models import FAQ
from contact.forms import ContactForm
import pprint

# from landing_page.forms import EmailCaptureForm



def faq_page(request):
	articles = Article.objects.filter(isLive=True).order_by('-PublishTime')
	articles.featured = list(articles.filter(isFeatured=True).order_by('-PublishTime'))[0:6]
	faqs = FAQ.objects.all().order_by('Rank')
	contact = ContactForm
	context = {'faqs': faqs, 'articles': articles, 'contact': contact}
	return render(request, 'faqs.html', context)	








			

