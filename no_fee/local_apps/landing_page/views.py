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
from urlparse import urlparse
from datetime import datetime
import json as simplejson
import string
from contact.forms import ContactForm
from models import LandingPageLead, BannerMedia
from articles.models import Article


def landing(request):
	articles = Article.objects.filter(isLive=True)[:12]
	lead = LandingPageLead.objects.filter(isLive=True)[0]
	banner = BannerMedia.objects.filter(isLive=True).latest('id')
	contact = ContactForm
	context = {'title':"rbh.me", 'contact': contact, 'banner': banner, 'lead': lead, 'articles': articles }
	return render(request, 'index.html', context) 
