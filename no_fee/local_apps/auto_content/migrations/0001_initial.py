# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ExtractedArticle'
        db.create_table(u'auto_content_extractedarticle', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Source', self.gf('django.db.models.fields.URLField')(default=None, max_length=255, null=True, blank=True)),
            ('HatTipHandle', self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, blank=True)),
            ('HatTipName', self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, blank=True)),
            ('TweetId', self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, blank=True)),
            ('TweetText', self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, blank=True)),
            ('TweetImage', self.gf('django.db.models.fields.URLField')(default=None, max_length=255, null=True, blank=True)),
            ('ArticleText', self.gf('django.db.models.fields.TextField')(default=None, null=True, blank=True)),
            ('ArticleImage', self.gf('django.db.models.fields.URLField')(default=None, max_length=255, null=True, blank=True)),
            ('ArticleMetaImage', self.gf('django.db.models.fields.URLField')(default=None, max_length=255, null=True, blank=True)),
            ('SaveTime', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('PublishTime', self.gf('django.db.models.fields.DateTimeField')(default=None, null=True, blank=True)),
            ('isLive', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('DescriptiveTitle', self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, blank=True)),
            ('MetaDescription', self.gf('django.db.models.fields.TextField')(default=None, max_length=300, null=True, blank=True)),
            ('ParentCategory', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['articles.ParentCategory'], null=True, blank=True)),
            ('Slug', self.gf('django.db.models.fields.SlugField')(default=None, max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'auto_content', ['ExtractedArticle'])


    def backwards(self, orm):
        # Deleting model 'ExtractedArticle'
        db.delete_table(u'auto_content_extractedarticle')


    models = {
        u'articles.parentcategory': {
            'CategoryLinkText': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'CategoryName': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'CategorySlug': ('django.db.models.fields.SlugField', [], {'max_length': '20'}),
            'Meta': {'ordering': "['CategoryName']", 'object_name': 'ParentCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'auto_content.extractedarticle': {
            'ArticleImage': ('django.db.models.fields.URLField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'ArticleMetaImage': ('django.db.models.fields.URLField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'ArticleText': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'DescriptiveTitle': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'HatTipHandle': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'HatTipName': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'Meta': {'ordering': "['-SaveTime']", 'object_name': 'ExtractedArticle'},
            'MetaDescription': ('django.db.models.fields.TextField', [], {'default': 'None', 'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'ParentCategory': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['articles.ParentCategory']", 'null': 'True', 'blank': 'True'}),
            'PublishTime': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'SaveTime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'Slug': ('django.db.models.fields.SlugField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'Source': ('django.db.models.fields.URLField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'TweetId': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'TweetImage': ('django.db.models.fields.URLField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'TweetText': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isLive': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['auto_content']