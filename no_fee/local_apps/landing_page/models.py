from django.db import models

class LandingPageLead(models.Model):
	LeadTitle = models.CharField(max_length=140, null=True, blank=True, default=None)
	LeadContent = models.TextField(max_length=500, null=True, default=False, blank=True)
	LandingMetaDescription = models.TextField(max_length=250, null=True, default=False, blank=True)
	isLive = models.BooleanField(blank=True, default=False)
	CreatedTime = models.DateTimeField(auto_now_add=True)
	
	def __unicode__(self):
		return u'%s | %s ' % (self.LeadTitle, self.CreatedTime)	

class BannerMedia(models.Model):
	BannerImage = models.ImageField(upload_to='home_banner', null=True, blank=True)
	BannerImageAsUrl = models.URLField(max_length=255,null=True, blank=True, default=None)
	BannerImageSourceName = models.CharField(max_length=255, null=True, blank=True, default=None)
	BannerImageSourceUrl = models.URLField(max_length=255,null=True, blank=True, default=None)
	BannerMediaName = models.CharField(max_length=140, null=True, blank=True, default=None)
	PublishTime = models.DateTimeField()
	isLive = models.BooleanField(blank=True, default=False)

	def __unicode__(self):
		return u'%s | Is Live: %s' % (self.BannerMediaName, self.isLive)

class DefaultSocialImage(models.Model):
	SocialImage = models.ImageField(upload_to='home_banner', null=True, blank=True)
	SocialImageAsUrl = models.URLField(max_length=255,null=True, blank=True, default=None)
	PublishTime = models.DateTimeField(auto_now_add=True)
	isLive = models.BooleanField(blank=True, default=False)

	def __unicode__(self):
		return u'%s  %s' % (self.BannerImage, self.BannerImageAsUrl)		
	

	# Author = models.ForeignKey(User)
	# Type = models.CharField(max_length=15, default="article", null=True, blank=True)
	# DraftTime = models.DateTimeField(auto_now_add=True)
	# PublishTime = models.DateTimeField()
	# isFeatured = models.BooleanField(blank=True, default=False)
	# PublishTime = models.DateTimeField()
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

