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
from models import CorpPage
import pprint

# from landing_page.forms import EmailCaptureForm



def corp_page(request, corp_slug):
	page = CorpPage.objects.get(PageSlug=corp_slug)
	context = {'page': page}
	return render(request, 'corp-pages.html', context)	








			

