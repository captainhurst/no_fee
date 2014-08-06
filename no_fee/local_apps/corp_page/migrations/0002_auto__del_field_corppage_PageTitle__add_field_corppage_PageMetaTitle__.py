# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'CorpPage.PageTitle'
        db.delete_column(u'corp_page_corppage', 'PageTitle')

        # Adding field 'CorpPage.PageMetaTitle'
        db.add_column(u'corp_page_corppage', 'PageMetaTitle',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CorpPage.PageMetaDescription'
        db.add_column(u'corp_page_corppage', 'PageMetaDescription',
                      self.gf('django.db.models.fields.TextField')(default=None, max_length=300, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'CorpPage.PageTitle'
        db.add_column(u'corp_page_corppage', 'PageTitle',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'CorpPage.PageMetaTitle'
        db.delete_column(u'corp_page_corppage', 'PageMetaTitle')

        # Deleting field 'CorpPage.PageMetaDescription'
        db.delete_column(u'corp_page_corppage', 'PageMetaDescription')


    models = {
        u'corp_page.corppage': {
            'DraftTime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'Meta': {'ordering': "['-DraftTime']", 'object_name': 'CorpPage'},
            'PageContentAsHTML': ('django.db.models.fields.TextField', [], {'default': 'None', 'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'PageMetaDescription': ('django.db.models.fields.TextField', [], {'default': 'None', 'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'PageMetaTitle': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'PageName': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'PageSlug': ('django.db.models.fields.SlugField', [], {'max_length': '30'}),
            'PublishTime': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isLive': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['corp_page']