# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'LandingPageLead'
        db.create_table(u'landing_page_landingpagelead', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('LeadTitle', self.gf('django.db.models.fields.CharField')(default=None, max_length=140, null=True, blank=True)),
            ('LeadContent', self.gf('django.db.models.fields.TextField')(default=False, max_length=500, null=True, blank=True)),
            ('LandingMetaDescription', self.gf('django.db.models.fields.TextField')(default=False, max_length=250, null=True, blank=True)),
            ('IsLive', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('CreatedTime', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'landing_page', ['LandingPageLead'])

        # Adding model 'BannerMedia'
        db.create_table(u'landing_page_bannermedia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('BannerYouTubeId', self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, blank=True)),
            ('BannerImage', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('BannerImageAsUrl', self.gf('django.db.models.fields.URLField')(default=None, max_length=255, null=True, blank=True)),
            ('BannerImageSourceName', self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, blank=True)),
            ('BannerImageSourceUrl', self.gf('django.db.models.fields.URLField')(default=None, max_length=255, null=True, blank=True)),
            ('BannerMediaName', self.gf('django.db.models.fields.CharField')(default=None, max_length=140, null=True, blank=True)),
            ('PublishTime', self.gf('django.db.models.fields.DateTimeField')()),
            ('isLive', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'landing_page', ['BannerMedia'])


    def backwards(self, orm):
        # Deleting model 'LandingPageLead'
        db.delete_table(u'landing_page_landingpagelead')

        # Deleting model 'BannerMedia'
        db.delete_table(u'landing_page_bannermedia')


    models = {
        u'landing_page.bannermedia': {
            'BannerImage': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'BannerImageAsUrl': ('django.db.models.fields.URLField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'BannerImageSourceName': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'BannerImageSourceUrl': ('django.db.models.fields.URLField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'BannerMediaName': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'BannerYouTubeId': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'BannerMedia'},
            'PublishTime': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isLive': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'landing_page.landingpagelead': {
            'CreatedTime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'IsLive': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'LandingMetaDescription': ('django.db.models.fields.TextField', [], {'default': 'False', 'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'LeadContent': ('django.db.models.fields.TextField', [], {'default': 'False', 'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'LeadTitle': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'LandingPageLead'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['landing_page']