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
# from articles.models import ArticleCategoryModel, ArticlePageModel
#from models import LandingPageModel, LandingPageMeta, EmailCaptureModel, LandingImageContentModel, LandingContent
#from forms import EmailCaptureForm

def landing(request):
	#title = LandingPageModel.objects.all().order_by("-id")[0]
	#meta = LandingPageMeta.objects.all().order_by("-id")[0]
	#ss_con = LandingImageContentModel.objects.all().order_by("-id")[0]
	#ssc = LandingContent.objects.all().order_by("rank")
	#featured = ArticleCategoryModel.objects.all()
	#for f in featured:
	#	f.list = ArticlePageModel.objects.filter(id=f.id).order_by('-created_datetime')[2]
	#articles = ArticlePageModel.objects.all().order_by("-created_datetime")[:5]
	#ecForm = EmailCaptureForm()
	#context = {'title': title, 'meta': meta, 'ss': ss_con, 'featured': featured, 'seo': ssc}
	contact = ContactForm
	context = {'title':"rbh.me", 'contact': contact}
	return render(request, 'index.html', context) 
	
# def email_capture(request):
# 	if request.POST:
# 		emailCapture = EmailCaptureForm(request.POST)
# 		if emailCapture.is_valid():
# 			emailCapture.save()
# 			return HttpResponse(True)
# 		else:
# 			return HttpResponse("invalid")
# 	else:
# 		return HttpResponse(False)