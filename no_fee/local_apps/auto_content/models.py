from django.db import models
from django.contrib.auth.models import User
# from story_arc.models import StoryArc
from articles.models import Category, StoryArc
from taggit.managers import TaggableManager


# Create your models here.
class ExtractedArticle(models.Model):
	Source = models.URLField(max_length=255,null=True, blank=True, default=None)
	HatTipHandle = models.CharField(max_length=255, null=True, blank=True, default=None)
	Type = models.CharField(max_length=10, default="extracted")
	HatTipName = models.CharField(max_length=255, null=True, blank=True, default=None)
	TweetId = models.CharField(max_length=255, null=True, blank=True, default=None, unique=True)
	TweetText = models.CharField(max_length=255, null=True, blank=True, default=None)
	TweetImage = models.CharField(max_length=255,null=True, blank=True, default=None)
	RawArticleText = models.TextField(null=True, blank=True, default=None)
	ArticleText = models.TextField(null=True, blank=True, default=None)
	ArticleImage = models.CharField(max_length=255,null=True, blank=True, default=None)
	ArticleMetaImage = models.URLField(max_length=255,null=True, blank=True, default=None)
	ArticleVideoLead = models.CharField(max_length=255,null=True, blank=True, default=None)
	SaveTime = models.DateTimeField(auto_now_add=True)
	PublishTime = models.DateTimeField(null=True, blank=True, default=None)
	isLive = models.BooleanField(blank=True, default=False)
	DescriptiveTitle = models.CharField(max_length=255, null=True, blank=True, default=None)
	MetaDescription = models.TextField(max_length=300, null=True, blank=True, default=None)
	ParentCategory = models.ForeignKey(Category, null=True, blank=True, default=None)
	Slug = models.SlugField(max_length=255, null=True, blank=True, default=None)
	StoryArc = models.ForeignKey(StoryArc, limit_choices_to = {'isLive':True}, null=True, blank=True, default=None)
	Tags = TaggableManager()

	def __unicode__(self):
		return u'** Is Live: %s **| %s | %s | %s' % (self.isLive, self.HatTipName, self.TweetText, self.SaveTime)	
	
	class Meta:
		ordering = ['-SaveTime']