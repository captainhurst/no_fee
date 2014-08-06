# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FAQ'
        db.create_table(u'faqs_faq', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('DraftTime', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('PublishTime', self.gf('django.db.models.fields.DateTimeField')()),
            ('Rank', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('isLive', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('Question', self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, blank=True)),
            ('Answer', self.gf('django.db.models.fields.TextField')(default=None, max_length=300, null=True, blank=True)),
        ))
        db.send_create_signal(u'faqs', ['FAQ'])


    def backwards(self, orm):
        # Deleting model 'FAQ'
        db.delete_table(u'faqs_faq')


    models = {
        u'faqs.faq': {
            'Answer': ('django.db.models.fields.TextField', [], {'default': 'None', 'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'DraftTime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'Meta': {'ordering': "['-DraftTime']", 'object_name': 'FAQ'},
            'PublishTime': ('django.db.models.fields.DateTimeField', [], {}),
            'Question': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'Rank': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isLive': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['faqs']