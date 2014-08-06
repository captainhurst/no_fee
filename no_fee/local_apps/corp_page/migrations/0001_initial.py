# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CorpPage'
        db.create_table(u'corp_page_corppage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('DraftTime', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('PublishTime', self.gf('django.db.models.fields.DateTimeField')()),
            ('PageName', self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, blank=True)),
            ('PageTitle', self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, blank=True)),
            ('PageSlug', self.gf('django.db.models.fields.SlugField')(max_length=30)),
            ('isLive', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('PageContentAsHTML', self.gf('django.db.models.fields.TextField')(default=None, max_length=300, null=True, blank=True)),
        ))
        db.send_create_signal(u'corp_page', ['CorpPage'])


    def backwards(self, orm):
        # Deleting model 'CorpPage'
        db.delete_table(u'corp_page_corppage')


    models = {
        u'corp_page.corppage': {
            'DraftTime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'Meta': {'ordering': "['-DraftTime']", 'object_name': 'CorpPage'},
            'PageContentAsHTML': ('django.db.models.fields.TextField', [], {'default': 'None', 'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'PageName': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'PageSlug': ('django.db.models.fields.SlugField', [], {'max_length': '30'}),
            'PageTitle': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'PublishTime': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isLive': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['corp_page']