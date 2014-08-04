# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'ArticleMedia.SlideshowType'
        db.delete_column(u'articles_articlemedia', 'SlideshowType')

        # Deleting field 'ArticleMedia.BannerImageText'
        db.delete_column(u'articles_articlemedia', 'BannerImageText')

        # Deleting field 'ArticleMedia.BannerImageAsUrl'
        db.delete_column(u'articles_articlemedia', 'BannerImageAsUrl')

        # Deleting field 'ArticleMedia.PreviewImage'
        db.delete_column(u'articles_articlemedia', 'PreviewImage')

        # Deleting field 'ArticleMedia.PreviewImageAsUrl'
        db.delete_column(u'articles_articlemedia', 'PreviewImageAsUrl')

        # Deleting field 'ArticleMedia.BannerImageTitle'
        db.delete_column(u'articles_articlemedia', 'BannerImageTitle')

        # Deleting field 'ArticleMedia.PreviewImageSourceUrl'
        db.delete_column(u'articles_articlemedia', 'PreviewImageSourceUrl')

        # Deleting field 'ArticleMedia.BannerImageSource'
        db.delete_column(u'articles_articlemedia', 'BannerImageSource')

        # Deleting field 'ArticleMedia.SocialImage'
        db.delete_column(u'articles_articlemedia', 'SocialImage')

        # Deleting field 'ArticleMedia.PreviewImageSource'
        db.delete_column(u'articles_articlemedia', 'PreviewImageSource')

        # Deleting field 'ArticleMedia.BannerImageSourceUrl'
        db.delete_column(u'articles_articlemedia', 'BannerImageSourceUrl')

        # Deleting field 'ArticleMedia.SocialImageAsUrl'
        db.delete_column(u'articles_articlemedia', 'SocialImageAsUrl')

        # Deleting field 'ArticleMedia.BannerImage'
        db.delete_column(u'articles_articlemedia', 'BannerImage')


    def backwards(self, orm):
        # Adding field 'ArticleMedia.SlideshowType'
        db.add_column(u'articles_articlemedia', 'SlideshowType',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=30),
                      keep_default=False)

        # Adding field 'ArticleMedia.BannerImageText'
        db.add_column(u'articles_articlemedia', 'BannerImageText',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ArticleMedia.BannerImageAsUrl'
        db.add_column(u'articles_articlemedia', 'BannerImageAsUrl',
                      self.gf('django.db.models.fields.URLField')(default=None, max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ArticleMedia.PreviewImage'
        db.add_column(u'articles_articlemedia', 'PreviewImage',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ArticleMedia.PreviewImageAsUrl'
        db.add_column(u'articles_articlemedia', 'PreviewImageAsUrl',
                      self.gf('django.db.models.fields.URLField')(default=None, max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ArticleMedia.BannerImageTitle'
        db.add_column(u'articles_articlemedia', 'BannerImageTitle',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ArticleMedia.PreviewImageSourceUrl'
        db.add_column(u'articles_articlemedia', 'PreviewImageSourceUrl',
                      self.gf('django.db.models.fields.URLField')(default=None, max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ArticleMedia.BannerImageSource'
        db.add_column(u'articles_articlemedia', 'BannerImageSource',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ArticleMedia.SocialImage'
        db.add_column(u'articles_articlemedia', 'SocialImage',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ArticleMedia.PreviewImageSource'
        db.add_column(u'articles_articlemedia', 'PreviewImageSource',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ArticleMedia.BannerImageSourceUrl'
        db.add_column(u'articles_articlemedia', 'BannerImageSourceUrl',
                      self.gf('django.db.models.fields.URLField')(default=None, max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ArticleMedia.SocialImageAsUrl'
        db.add_column(u'articles_articlemedia', 'SocialImageAsUrl',
                      self.gf('django.db.models.fields.URLField')(default=None, max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ArticleMedia.BannerImage'
        db.add_column(u'articles_articlemedia', 'BannerImage',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)


    models = {
        u'articles.article': {
            'ArticleMedia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['articles.ArticleMedia']"}),
            'ArticleText': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'Author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'Description': ('django.db.models.fields.TextField', [], {'default': 'None', 'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'DraftTime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'FeaturedArticle': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'article'", 'symmetrical': 'False', 'through': u"orm['articles.FeaturedArticle']", 'to': u"orm['articles.Article']"}),
            'Meta': {'ordering': "['-DraftTime']", 'unique_together': "(('Slug', 'ParentCategory'),)", 'object_name': 'Article'},
            'ParentCategory': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['articles.Category']"}),
            'PublishTime': ('django.db.models.fields.DateTimeField', [], {}),
            'Slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'Subtitle': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'Title': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'Type': ('django.db.models.fields.CharField', [], {'default': "'article'", 'max_length': '15', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isFeatured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isLive': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'articles.articlemedia': {
            'ArticleImage': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'ArticleImageAsUrl': ('django.db.models.fields.URLField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'ArticleImageSource': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'ArticleImageSourceUrl': ('django.db.models.fields.URLField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'ArticleMedia'},
            'YouTubeId': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'articles.category': {
            'CategoryLinkText': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'CategoryName': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'CategorySlug': ('django.db.models.fields.SlugField', [], {'max_length': '20'}),
            'Meta': {'ordering': "['CategoryName']", 'object_name': 'Category'},
            'ParentCategory': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['articles.Category']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        u'articles.featuredarticle': {
            'ArticleIn': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'an_attached_featured_article'", 'to': u"orm['articles.Article']"}),
            'ArticleSelf': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'the_article_itself'", 'to': u"orm['articles.Article']"}),
            'Meta': {'object_name': 'FeaturedArticle'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['articles']