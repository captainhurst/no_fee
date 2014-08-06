from django.db import models
from django.contrib.auth.models import User
from utils import *
# from taggit.models import TagBase, ItemBase



class FAQ(models.Model):
	DraftTime = models.DateTimeField(auto_now_add=True)
	PublishTime = models.DateTimeField()
	Rank = models.IntegerField(blank=True, default=False)
	isLive = models.BooleanField(blank=True, default=False)
	Question = models.CharField(max_length=255, null=True, blank=True, default=None)
	Answer = models.TextField(max_length=300, null=True, blank=True, default=None)
	

	def __unicode__(self):
		return u'Rank: %s| %s | %s ' % (self.Rank, self.Question, self.PublishTime)	
	
	class Meta:
		ordering = ['-DraftTime']





