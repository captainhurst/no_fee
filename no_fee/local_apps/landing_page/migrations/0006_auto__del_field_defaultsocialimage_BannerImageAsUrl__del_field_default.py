# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'DefaultSocialImage.BannerImageAsUrl'
        db.delete_column(u'landing_page_defaultsocialimage', 'BannerImageAsUrl')

        # Deleting field 'DefaultSocialImage.BannerImage'
        db.delete_column(u'landing_page_defaultsocialimage', 'BannerImage')

        # Adding field 'DefaultSocialImage.SocialImage'
        db.add_column(u'landing_page_defaultsocialimage', 'SocialImage',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DefaultSocialImage.SocialImageAsUrl'
        db.add_column(u'landing_page_defaultsocialimage', 'SocialImageAsUrl',
                      self.gf('django.db.models.fields.URLField')(default=None, max_length=255, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'DefaultSocialImage.BannerImageAsUrl'
        db.add_column(u'landing_page_defaultsocialimage', 'BannerImageAsUrl',
                      self.gf('django.db.models.fields.URLField')(default=None, max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DefaultSocialImage.BannerImage'
        db.add_column(u'landing_page_defaultsocialimage', 'BannerImage',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'DefaultSocialImage.SocialImage'
        db.delete_column(u'landing_page_defaultsocialimage', 'SocialImage')

        # Deleting field 'DefaultSocialImage.SocialImageAsUrl'
        db.delete_column(u'landing_page_defaultsocialimage', 'SocialImageAsUrl')


    models = {
        u'landing_page.bannermedia': {
            'BannerImage': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'BannerImageAsUrl': ('django.db.models.fields.URLField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'BannerImageSourceName': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'BannerImageSourceUrl': ('django.db.models.fields.URLField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'BannerMediaName': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'BannerMedia'},
            'PublishTime': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isLive': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'landing_page.defaultsocialimage': {
            'Meta': {'object_name': 'DefaultSocialImage'},
            'PublishTime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'SocialImage': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'SocialImageAsUrl': ('django.db.models.fields.URLField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isLive': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'landing_page.landingpagelead': {
            'CreatedTime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'LandingMetaDescription': ('django.db.models.fields.TextField', [], {'default': 'False', 'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'LeadContent': ('django.db.models.fields.TextField', [], {'default': 'False', 'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'LeadTitle': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'LandingPageLead'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isLive': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['landing_page']