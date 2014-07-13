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
from urlparse import urlparse
from datetime import datetime
import json as simplejson
import string

def story_arc(request):
	# page = ArticlePageModel.objects.get(descriptive_url=article_slug)
	# ecForm = EmailCaptureForm()
	
	# featured = ArticleCategoryModel.objects.filter(category_slug=category)
	
	# fd = ArticlePageModel.objects.filter(category=featured).order_by('-created_datetime')
	# context = {'page': page, 'featured': fd, 'ecForm': ecForm}
	return render(request, 'story_arc.html')	


def get_story_arc(request, category, story_slug):
	# page = ArticlePageModel.objects.get(descriptive_url=article_slug)
	# ecForm = EmailCaptureForm()
	
	# featured = ArticleCategoryModel.objects.filter(category_slug=category)
	
	# fd = ArticlePageModel.objects.filter(category=featured).order_by('-created_datetime')
	# context = {'page': page, 'featured': fd, 'ecForm': ecForm}
	return render(request, 'story_arc.html')		


		

