# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.template import RequestContext, loader
from django.contrib import auth
from django.conf import settings as conf_settings
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.sites.models import Site
from django.contrib.sites.models import get_current_site
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.db import IntegrityError
from django.core.cache import cache
from django.db.models import Q
from urlparse import urlparse
from datetime import datetime
from itertools import chain
from mptt.utils import drilldown_tree_for_node
from django.db.models.query import EmptyQuerySet
from models import ArticleMedia, FeaturedProduct, Article, SlideshowBanner, FeaturedArticle, Category

import pprint

# from landing_page.forms import EmailCaptureForm


def get_article(request, category, article_slug):
	slug_components = article_slug.split('/')
	try:
		pc = Category.objects.get(CategorySlug=category)
		subs = pc.get_children()
		page = Article.objects.prefetch_related().get(Slug=slug_components[-1])
		articles = Article.objects.filter(ParentCategory__ParentCategory_id=pc.id).exclude(id=page.id).order_by('-PublishTime')[:6]
		stories = StoryArc.objects.filter(Q(isLive=True), Q(ParentCategory__ParentCategory_id=pc.id) | Q(ParentCategory__id=pc.id)).order_by('-PublishTime')[:6]
		page.recent = list(chain(articles, extracted, stories))[0:10]
		print page.recent
		context = {'subnav': subs, 'page': page, 'isArticle': True }
		return render(request, 'article-video-hybrid.html', context)
	except:
		pass
	try:
		pc = Category.objects.get(CategorySlug=category)
		subs = pc.get_children()
		page = ExtractedArticle.objects.prefetch_related().get(Slug=slug_components[-1])
		articles = Article.objects.filter(ParentCategory__ParentCategory_id=pc.id).order_by('-PublishTime')[:6]
		stories = StoryArc.objects.filter(Q(isLive=True), Q(ParentCategory__ParentCategory_id=pc.id) | Q(ParentCategory__id=pc.id)).order_by('-PublishTime')[:6]		
		page.recent = list(chain(articles,extracted, stories))[0:10]
		print page.recent
		context = {'subnav': subs, 'page': page, 'isArticle': False }
		return render(request, 'article-video-hybrid.html', context)
	except:
		pc = Category.objects.get(CategorySlug=slug_components[-1])
		subs = pc.get_root().get_children()
		articles = Article.objects.filter(Q(isLive=True), Q(ParentCategory__ParentCategory_id=pc.id) | Q(ParentCategory__id=pc.id)).order_by('-PublishTime')
		articles.featured = articles.filter(isFeatured=True).order_by('-PublishTime')
		section = articles.filter(isFeatured=False).order_by('-PublishTime')
		stories = StoryArc.objects.filter(Q(isLive=True), Q(ParentCategory__ParentCategory_id=pc.id) | Q(ParentCategory__id=pc.id)).order_by('-PublishTime')[:6]		
		articles.section = list(chain(section, stories, extracted))[0:16]
		context = {'subnav': subs, 'articles': articles, "category": pc}
		return render(request, 'listed-articles.html', context)


def get_category(request, category):
	pc = Category.objects.get(CategorySlug=category)
	subs = pc.get_children()
	articles = Article.objects.filter(Q(isLive=True), Q(ParentCategory__ParentCategory_id=pc.id) | Q(ParentCategory__id=pc.id)).order_by('-PublishTime')
	articles.featured = articles.filter(isFeatured=True).order_by('-PublishTime')
	articles.section = articles.filter(isFeatured=False).order_by('-PublishTime')
	context = {'subnav': subs, 'articles': articles }
	return render(request, 'index-category.html', context)	








			

