# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'FAQ.Rank'
        db.alter_column(u'faqs_faq', 'Rank', self.gf('django.db.models.fields.IntegerField')())

    def backwards(self, orm):

        # Changing field 'FAQ.Rank'
        db.alter_column(u'faqs_faq', 'Rank', self.gf('django.db.models.fields.BooleanField')())

    models = {
        u'faqs.faq': {
            'Answer': ('django.db.models.fields.TextField', [], {'default': 'None', 'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'DraftTime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'Meta': {'ordering': "['-DraftTime']", 'object_name': 'FAQ'},
            'PublishTime': ('django.db.models.fields.DateTimeField', [], {}),
            'Question': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'Rank': ('django.db.models.fields.IntegerField', [], {'default': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isLive': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['faqs']