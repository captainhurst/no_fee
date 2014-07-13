from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
	User = models.OneToOneField(User, related_name='profile')
	InstagramUserName = models.CharField(max_length=255, null=True, blank=True, default=None, unique=True)
	TwitterUserName = models.CharField(max_length=255, null=True, blank=True, default=None, unique=True)
	FacebookUrl = models.URLField(max_length=255,null=True, blank=True, default=None, unique=True)

	def __unicode__(self):
		return u'%s %s' % (self.User.first_name, self.User.last_name)	
