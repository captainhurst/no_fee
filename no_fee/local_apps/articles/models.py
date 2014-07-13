from django.db import models
from django.contrib.auth.models import User
from utils import *
# from taggit.models import TagBase, ItemBase
from mptt.models import MPTTModel, TreeForeignKey
from taggit.managers import TaggableManager
# from treebeard.mp_tree import MP_Node
# from scaffold.models import BaseSection
from south.modelsinspector import add_ignored_fields
add_ignored_fields(["^taggit\.managers"])


class Category(MPTTModel):
	CategoryName = models.CharField(max_length=80, null=True, blank=True, default=None)
	CategoryLinkText = models.CharField(max_length=40, null=True, blank=True, default=None)
	CategorySlug = models.SlugField(max_length=20)
	ParentCategory = TreeForeignKey('self', null=True, blank=True, related_name='children')

	class MPTTMeta:
		order_insertion_by = ['CategoryName']
		parent_attr = 'ParentCategory'

	def __unicode__(self):
		return u'%s' % (self.CategoryName)
	
	class Meta:
		ordering = ['CategoryName']	


class ArticleMedia(models.Model):
	BANNER_CHOICES = (
		('video', 'Video Lead'),
		('image', 'Image Lead'),
		( False, 'No Media'),		
		)
	SlideshowType = models.CharField(max_length=30,choices=BANNER_CHOICES)
	BannerImage = models.ImageField(upload_to='banner', null=True, blank=True)
	BannerImageAsUrl = models.URLField(max_length=255,null=True, blank=True, default=None)
	BannerImageTitle = models.CharField(max_length=255,null=True, blank=True, default=None)
	BannerImageText = models.CharField(max_length=255,null=True, blank=True, default=None)
	BannerImageSource = models.CharField(max_length=255, null=True, blank=True, default=None)
	BannerImageSourceUrl = models.URLField(max_length=255,null=True, blank=True, default=None)
	YouTubeId = models.CharField(max_length=255,null=True, blank=True, default=None)
	PreviewImage = models.ImageField(upload_to='artcle_preview', null=True, blank=True)
	PreviewImageAsUrl = models.URLField(max_length=255,null=True, blank=True, default=None)
	PreviewImageSource = models.CharField(max_length=255, null=True, blank=True, default=None)
	PreviewImageSourceUrl = models.URLField(max_length=255,null=True, blank=True, default=None)
	ArticleImage = models.ImageField(upload_to='article', null=True, blank=True)
	ArticleImageAsUrl = models.URLField(max_length=255,null=True, blank=True, default=None)
	ArticleImageSource = models.CharField(max_length=255, null=True, blank=True, default=None)
	ArticleImageSourceUrl = models.URLField(max_length=255,null=True, blank=True, default=None)
	SocialImage = models.ImageField(upload_to='meta', null=True, blank=True)
	SocialImageAsUrl = models.URLField(max_length=255,null=True, blank=True, default=None)

	def __unicode__(self):
		return u'%s | %s' % (self.BannerImageTitle, self.BannerImageTitle)

class FeaturedProduct(models.Model):
	IsCategoryDefault = models.BooleanField()
	ProductImage = models.ImageField(upload_to='product')
	ProductName = models.CharField(max_length=255, null=True, blank=True, default=None)
	AffiliateLink = models.CharField(max_length=255, null=True, blank=True, default=None)

	def __unicode__(self):
		return u'%s' % (self.ProductName)

class Article(models.Model):
	Author = models.ForeignKey(User)
	Type = models.CharField(max_length=15, default="article", null=True, blank=True)
	DraftTime = models.DateTimeField(auto_now_add=True)
	PublishTime = models.DateTimeField()
	isFeatured = models.BooleanField(blank=True, default=False)
	isLive = models.BooleanField(blank=True, default=False)
	Title = models.CharField(max_length=255, null=True, blank=True, default=None)
	Description = models.TextField(max_length=300, null=True, blank=True, default=None)
	Subtitle = models.CharField(max_length=255, null=True, blank=True, default=None)
	ArticleText = models.TextField(null=True, blank=True, default=None)
	ArticleMedia = models.ForeignKey(ArticleMedia)
	FeaturedProducts = models.ManyToManyField(FeaturedProduct)
	ParentCategory = models.ForeignKey(Category)
	Slug = models.SlugField(max_length=255)
	FeaturedArticle = models.ManyToManyField('self', through='FeaturedArticle', symmetrical=False, related_name='article')
	Tags = TaggableManager()

	def __unicode__(self):
		return u'%s | %s | %s' % (self.Title, self.PublishTime, self.Slug)	
	
	class Meta:
		unique_together = ('Slug', 'ParentCategory')
		ordering = ['-DraftTime']

class SlideshowBanner(models.Model):
	SlideshowBannerName = models.CharField(max_length=80, null=True, blank=True, default=None)
	ParentCategory = models.ForeignKey(Category, null=True, blank=True)
	SLIDESHOW_CHOICES = (
		('banner', 'Banner Only'),
		('featured', 'Banner w/Features'),		
		)
	SlideshowType = models.CharField(max_length=30,choices=SLIDESHOW_CHOICES)
	SlideshowArticles = models.ManyToManyField(Article)		

	def __unicode__(self):
		return u'%s' % (self.SlideshowBannerName)

class FeaturedArticle(models.Model):
	ArticleSelf = models.ForeignKey(Article, related_name='the_article_itself')
	ArticleIn = models.ForeignKey(Article,  related_name='an_attached_featured_article')






