from django.db import models
from django.contrib.auth.models import User
# from articles.models import ParentCategory, FeaturedProduct, ArticleMedia
# from utils import *
# # Create your models here.



# class StoryArc(models.Model):
# 	StoryAuthor = models.ForeignKey(User, blank=True, default=None, null=True)
# 	DraftTime = models.DateTimeField(auto_now_add=True)
# 	isLive = models.BooleanField(blank=True, default=False)
# 	PublishTime = models.DateTimeField()
# 	isFeatured = models.BooleanField(blank=True, default=False)
# 	StoryTitle = models.CharField(max_length=255, null=True, blank=True, default=None)
# 	StoryDescription = models.TextField(max_length=300, null=True, blank=True, default=None)
# 	StorySubtitle = models.CharField(max_length=255, null=True, blank=True, default=None)
# 	StoryText = models.TextField(null=True, blank=True, default=None)
# 	StoryMedia = models.ForeignKey(ArticleMedia)
# 	FeaturedProducts = models.ManyToManyField(FeaturedProduct)
# 	# SideBarComponents = models.ForeignKey(User, null=True)
# 	ParentCategory = models.ForeignKey(ParentCategory)
# 	# SubCategory = models.ForeignKey(SubCategory)
# 	StorySlug = models.SlugField(max_length=255)
	
# 	def __unicode__(self):
# 		return u'%s | %s | %s' % (self.StoryTitle, self.Slug,  self.PublishTime,)	
	
# 	class Meta:
# 		ordering = ['-DraftTime']


# Add the ability to follow story arcs - users can opt into email updates about specific stories
# Add functionality to allow users to create profiles and have timelines of news articles/stories
	# Follow Story arcs and categories and authors
	# Newsfeed of preferred content/authors
# Add functionality to allow users to create their own story arcs
# Add comment functionality that requires all responses to articles/story arcs/ editorials be blog posts as well
	# No cascading comments - facilitate long form argument in comments
