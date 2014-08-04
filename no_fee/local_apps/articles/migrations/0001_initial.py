# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'articles_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('CategoryName', self.gf('django.db.models.fields.CharField')(default=None, max_length=80, null=True, blank=True)),
            ('CategoryLinkText', self.gf('django.db.models.fields.CharField')(default=None, max_length=40, null=True, blank=True)),
            ('CategorySlug', self.gf('django.db.models.fields.SlugField')(max_length=20)),
            ('ParentCategory', self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='children', null=True, to=orm['articles.Category'])),
            (u'lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal(u'articles', ['Category'])

        # Adding model 'ArticleMedia'
        db.create_table(u'articles_articlemedia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('SlideshowType', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('BannerImage', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('BannerImageAsUrl', self.gf('django.db.models.fields.URLField')(default=None, max_length=255, null=True, blank=True)),
            ('BannerImageTitle', self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, blank=True)),
            ('BannerImageText', self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, blank=True)),
            ('BannerImageSource', self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, blank=True)),
            ('BannerImageSourceUrl', self.gf('django.db.models.fields.URLField')(default=None, max_length=255, null=True, blank=True)),
            ('YouTubeId', self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, blank=True)),
            ('PreviewImage', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('PreviewImageAsUrl', self.gf('django.db.models.fields.URLField')(default=None, max_length=255, null=True, blank=True)),
            ('PreviewImageSource', self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, blank=True)),
            ('PreviewImageSourceUrl', self.gf('django.db.models.fields.URLField')(default=None, max_length=255, null=True, blank=True)),
            ('ArticleImage', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('ArticleImageAsUrl', self.gf('django.db.models.fields.URLField')(default=None, max_length=255, null=True, blank=True)),
            ('ArticleImageSource', self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, blank=True)),
            ('ArticleImageSourceUrl', self.gf('django.db.models.fields.URLField')(default=None, max_length=255, null=True, blank=True)),
            ('SocialImage', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('SocialImageAsUrl', self.gf('django.db.models.fields.URLField')(default=None, max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'articles', ['ArticleMedia'])

        # Adding model 'Article'
        db.create_table(u'articles_article', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('Type', self.gf('django.db.models.fields.CharField')(default='article', max_length=15, null=True, blank=True)),
            ('DraftTime', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('PublishTime', self.gf('django.db.models.fields.DateTimeField')()),
            ('isFeatured', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('isLive', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('Title', self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, blank=True)),
            ('Description', self.gf('django.db.models.fields.TextField')(default=None, max_length=300, null=True, blank=True)),
            ('Subtitle', self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, blank=True)),
            ('ArticleText', self.gf('django.db.models.fields.TextField')(default=None, null=True, blank=True)),
            ('ArticleMedia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['articles.ArticleMedia'])),
            ('ParentCategory', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['articles.Category'])),
            ('Slug', self.gf('django.db.models.fields.SlugField')(max_length=255)),
        ))
        db.send_create_signal(u'articles', ['Article'])

        # Adding unique constraint on 'Article', fields ['Slug', 'ParentCategory']
        db.create_unique(u'articles_article', ['Slug', 'ParentCategory_id'])

        # Adding model 'FeaturedArticle'
        db.create_table(u'articles_featuredarticle', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ArticleSelf', self.gf('django.db.models.fields.related.ForeignKey')(related_name='the_article_itself', to=orm['articles.Article'])),
            ('ArticleIn', self.gf('django.db.models.fields.related.ForeignKey')(related_name='an_attached_featured_article', to=orm['articles.Article'])),
        ))
        db.send_create_signal(u'articles', ['FeaturedArticle'])


    def backwards(self, orm):
        # Removing unique constraint on 'Article', fields ['Slug', 'ParentCategory']
        db.delete_unique(u'articles_article', ['Slug', 'ParentCategory_id'])

        # Deleting model 'Category'
        db.delete_table(u'articles_category')

        # Deleting model 'ArticleMedia'
        db.delete_table(u'articles_articlemedia')

        # Deleting model 'Article'
        db.delete_table(u'articles_article')

        # Deleting model 'FeaturedArticle'
        db.delete_table(u'articles_featuredarticle')


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
            'BannerImage': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'BannerImageAsUrl': ('django.db.models.fields.URLField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'BannerImageSource': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'BannerImageSourceUrl': ('django.db.models.fields.URLField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'BannerImageText': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'BannerImageTitle': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'ArticleMedia'},
            'PreviewImage': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'PreviewImageAsUrl': ('django.db.models.fields.URLField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'PreviewImageSource': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'PreviewImageSourceUrl': ('django.db.models.fields.URLField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'SlideshowType': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'SocialImage': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'SocialImageAsUrl': ('django.db.models.fields.URLField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
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