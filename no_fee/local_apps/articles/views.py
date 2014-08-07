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
from models import ArticleMedia, Article, FeaturedArticle, Category
from contact.forms import ContactForm
import pprint

# from landing_page.forms import EmailCaptureForm


def get_article(request, category, article_slug):
	slug_components = article_slug.split('/')
	try:
		pc = Category.objects.get(CategorySlug=category)
		subs = pc.get_children()
		print u'%s - subs' % (subs)
		page = Article.objects.prefetch_related().get(Slug=slug_components[-1])
		print u'%s - page' % (page)
		print pc.id
		page.recent = Article.objects.filter(Q(ParentCategory__ParentCategory_id=pc.id) | Q(ParentCategory__id=pc.id)).exclude(id=page.id).order_by('-PublishTime')[:6]
		print u'%s - articles' % (page.recent)
		# page.recent = articles
		contact = ContactForm		
		context = {'subnav': subs, 'page': page, 'contact': contact, "category": pc}
		print pc
		return render(request, 'article-video-hybrid.html', context)
	except:
		pc = Category.objects.get(CategorySlug=slug_components[-1])
		print pc
		subs = pc.get_root().get_children()
		articles = Article.objects.filter(Q(isLive=True), Q(ParentCategory__ParentCategory_id=pc.id) | Q(ParentCategory__id=pc.id)).order_by('-PublishTime')
		articles.featured = articles.filter(isFeatured=True).order_by('-PublishTime')
		section = articles.filter(isFeatured=False).order_by('-PublishTime')
		articles.section = section[0:16]
		contact = ContactForm
		context = {'subnav': subs, 'articles': articles, "category": pc, 'contact': contact}
		return render(request, 'listed-articles.html', context)


def get_category(request, category):
	pc = Category.objects.get(CategorySlug=category)
	subs = pc.get_children()
	articles = Article.objects.filter(Q(isLive=True), Q(ParentCategory__ParentCategory_id=pc.id) | Q(ParentCategory__id=pc.id)).order_by('-PublishTime')
	# extracted = list(ExtractedArticle.objects.filter(Q(isLive=True), Q(ParentCategory__ParentCategory_id=pc.id) | Q(ParentCategory__id=pc.id)))
	# articles.featured = list(articles.filter(isFeatured=True).order_by('-PublishTime'))
	section = list(articles.filter(isFeatured=False).order_by('-PublishTime'))
	# stories = list(StoryArc.objects.filter(Q(isLive=True), Q(ParentCategory__ParentCategory_id=pc.id) | Q(ParentCategory__id=pc.id)).order_by('-PublishTime'))	
	# while len(articles.featured) <= 1:
	# 	if len(stories) > 0:
	# 		articles.featured.append(stories[0])
	# 		stories.pop(0)
	# 		print "stories"
	# 	elif len(section) > 0:
	# 		articles.featured.append(section[0])
	# 		section.pop(0)
	# 		print "section"
	# 	elif len(extracted) > 0:
	# 		articles.featured.append(extracted[0])
	# 		extracted.pop(0)
	# 		print extracted
	# 	else:
	# 		break
	articles.section = list(chain(section))
	context = {'subnav': subs, 'articles': articles }
	return render(request, 'index-category.html', context)	








			

