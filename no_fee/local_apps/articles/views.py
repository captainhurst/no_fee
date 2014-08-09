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
from models import ArticleMedia, Article, FeaturedArticle, Category
from contact.forms import ContactForm
import pprint

# from landing_page.forms import EmailCaptureForm


def get_article(request, category, article_slug):
	slug_components = article_slug.split('/')
	try:
		page = Article.objects.prefetch_related().get(Slug=slug_components[-1])
		pc = Category.objects.get(CategorySlug=category)
		page.recent = Article.objects.filter(Q(isLive=True), Q(ParentCategory__ParentCategory_id=pc.id) | Q(ParentCategory__id=pc.id)).exclude(id=page.id).order_by('-PublishTime')[:6]
		contact = ContactForm		
		context = {'page': page, 'contact': contact, "category": pc}
		return render(request, 'article-video-hybrid.html', context)
	except:
		pc = Category.objects.get(CategorySlug=slug_components[-1])
		print pc.MetaCategoryPageTitle
		subs = pc.get_root().get_children()
		articles = Article.objects.prefetch_related().filter(Q(isLive=True), Q(ParentCategory__ParentCategory_id=pc.id) | Q(ParentCategory__id=pc.id)).order_by('-PublishTime')
		articles.featured = articles.filter(isFeatured=True).order_by('-PublishTime')
		section = articles.filter(isFeatured=False).order_by('-PublishTime')
		articles.section = section[0:16]
		contact = ContactForm
		context = {'subcat': subs, 'articles': articles, "category": pc, 'contact': contact}
		return render(request, 'listed-articles.html', context)


def get_category(request, category):
	pc = Category.objects.get(CategorySlug=category)
	subs = pc.get_children()
	articles = Article.objects.filter(Q(isLive=True), Q(ParentCategory__ParentCategory_id=pc.id) | Q(ParentCategory__id=pc.id)).order_by('-PublishTime')
	articles.featured = list(articles.filter(isFeatured=True).order_by('-PublishTime'))
	articles.section = list(articles.filter(isFeatured=False).order_by('-PublishTime'))
	contact = ContactForm
	context = {'subcat': subs, 'category': pc, 'articles': articles, 'contact': contact }
	return render(request, 'index-category.html', context)	








			

