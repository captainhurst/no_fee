from django.db import models

class LandingPageLead(models.Model):
	LeadTitle = models.CharField(max_length=140, null=True, blank=True, default=None)
	LeadContent = models.TextField(max_length=500, null=True, default=False, blank=True)
	IsLive = models.BooleanField(blank=True, default=False)
	CreatedTime = models.DateTimeField(auto_now_add=True)
	
	def __unicode__(self):
		return u'%s | %s ' % (self.IsLive, self.CreatedTime)	


	# Author = models.ForeignKey(User)
	# Type = models.CharField(max_length=15, default="article", null=True, blank=True)
	# DraftTime = models.DateTimeField(auto_now_add=True)
	# PublishTime = models.DateTimeField()
	# isFeatured = models.BooleanField(blank=True, default=False)
	# isLive = models.BooleanField(blank=True, default=False)
	# Title = models.CharField(max_length=255, null=True, blank=True, default=None)
	# Description = models.TextField(max_length=300, null=True, blank=True, default=None)
	# Subtitle = models.CharField(max_length=255, null=True, blank=True, default=None)
	# ArticleText = models.TextField(null=True, blank=True, default=None)
	# ArticleMedia = models.ForeignKey(ArticleMedia)
	# FeaturedProducts = models.ManyToManyField(FeaturedProduct)
	# ParentCategory = models.ForeignKey(Category)
	# Slug = models.SlugField(max_length=255)
	# FeaturedArticle = models.ManyToManyField('self', through='FeaturedArticle', symmetrical=False, related_name='article')
	# Tags = TaggableManager()

	# def __unicode__(self):
	# 	return u'%s | %s | %s' % (self.Title, self.PublishTime, self.Slug)	
	
	# class Meta:
	# 	unique_together = ('Slug', 'ParentCategory')
	# 	ordering = ['-DraftTime']

