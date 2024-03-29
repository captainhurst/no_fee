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
# from landing_page.forms import EmailCaptureForm

from articles.models import Article


from forms import ContactForm

def contact(request):
	# ecForm = EmailCaptureForm()
	articles = Article.objects.filter(isFeatured=True).order_by('-PublishTime')[0:6]
	if request.method == 'POST':
		form = ContactForm(request.POST) # A form bound to the POST data
		if form.is_valid():
			subject = form.cleaned_data['subject']
			sender = form.cleaned_data['sender']
			message = form.cleaned_data['message'] + "     THIS MESSAGE IS FROM THE FOLLOWING EMAIL ADDRESS: "+ str(sender)
			recipients = [conf_settings.RECIPIENT_EMAIL_ADDRESS]
			from django.core.mail import send_mail
			send_mail(subject, message, sender, recipients)		
		context = { 'contact': form,'sent': True, 'articles': articles}
		return render(request, 'contact.html', context)
	else:	
		contact = ContactForm()
		context = {'contact': contact, 'sent': False, 'articles': articles}
		return render(request, 'contact.html', context)


	

