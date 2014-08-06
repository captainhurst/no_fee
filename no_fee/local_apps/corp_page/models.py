from django.db import models
from django.contrib.auth.models import User
from utils import *
# from taggit.models import TagBase, ItemBase



class CorpPage(models.Model):
	DraftTime = models.DateTimeField(auto_now_add=True)
	PublishTime = models.DateTimeField()
	PageName = models.CharField(max_length=255, null=True, blank=True, default=None)
	PageMetaTitle = models.CharField(max_length=255, null=True, blank=True, default=None)
	PageMetaDescription = models.TextField(max_length=300, null=True, blank=True, default=None)
	PageSlug = models.SlugField(max_length=30)
	isLive = models.BooleanField(blank=True, default=False)
	PageContentAsHTML = models.TextField(max_length=300, null=True, blank=True, default=None)
	

	def __unicode__(self):
		return u'%s| Live: %s | Publish: %s ' % (self.PageName, self.isLive, self.PublishTime)	
	
	class Meta:
		ordering = ['-DraftTime']





