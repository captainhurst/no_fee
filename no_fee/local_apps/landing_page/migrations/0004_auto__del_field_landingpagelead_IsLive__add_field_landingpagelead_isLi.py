# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'LandingPageLead.IsLive'
        db.delete_column(u'landing_page_landingpagelead', 'IsLive')

        # Adding field 'LandingPageLead.isLive'
        db.add_column(u'landing_page_landingpagelead', 'isLive',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'LandingPageLead.IsLive'
        db.add_column(u'landing_page_landingpagelead', 'IsLive',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Deleting field 'LandingPageLead.isLive'
        db.delete_column(u'landing_page_landingpagelead', 'isLive')


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