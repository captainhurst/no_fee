# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'StoryArc.ChildStories'
        db.add_column(u'story_arc_storyarc', 'ChildStories',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['auto_content.ExtractedArticle'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'StoryArc.ChildArticles'
        db.add_column(u'story_arc_storyarc', 'ChildArticles',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['articles.Article'], null=True, blank=True),
                      keep_default=False)

        # Removing M2M table for field ChildStories on 'StoryArc'
        db.delete_table(db.shorten_name(u'story_arc_storyarc_ChildStories'))


    def backwards(self, orm):
        # Deleting field 'StoryArc.ChildStories'
        db.delete_column(u'story_arc_storyarc', 'ChildStories_id')

        # Deleting field 'StoryArc.ChildArticles'
        db.delete_column(u'story_arc_storyarc', 'ChildArticles_id')

        # Adding M2M table for field ChildStories on 'StoryArc'
        m2m_table_name = db.shorten_name(u'story_arc_storyarc_ChildStories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('storyarc', models.ForeignKey(orm[u'story_arc.storyarc'], null=False)),
            ('article', models.ForeignKey(orm[u'articles.article'], null=False))
        ))
        db.create_unique(m2m_table_name, ['storyarc_id', 'article_id'])


    models = {
        u'articles.article': {
            'ArticleMedia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['articles.ArticleMedia']"}),
            'ArticleText': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'Author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'Description': ('django.db.models.fields.TextField', [], {'default': 'None', 'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'DraftTime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'FeaturedArticle': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'article'", 'symmetrical': 'False', 'through': u"orm['articles.FeaturedArticle']", 'to': u"orm['articles.Article']"}),
            'FeaturedProducts': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['articles.FeaturedProduct']", 'symmetrical': 'False'}),
            'Meta': {'ordering': "['-DraftTime']", 'object_name': 'Article'},
            'ParentCategory': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['articles.ParentCategory']"}),
            'PublishTime': ('django.db.models.fields.DateTimeField', [], {}),
            'Slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'Subtitle': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'Title': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
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
        u'articles.featuredarticle': {
            'ArticleIn': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'an_attached_featured_article'", 'to': u"orm['articles.Article']"}),
            'ArticleSelf': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'the_article_itself'", 'to': u"orm['articles.Article']"}),
            'Meta': {'object_name': 'FeaturedArticle'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'articles.featuredproduct': {
            'AffiliateLink': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'IsCategoryDefault': ('django.db.models.fields.BooleanField', [], {}),
            'Meta': {'object_name': 'FeaturedProduct'},
            'ProductImage': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'ProductName': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'articles.parentcategory': {
            'CategoryLinkText': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'CategoryName': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'CategorySlug': ('django.db.models.fields.SlugField', [], {'max_length': '20'}),
            'Meta': {'ordering': "['CategoryName']", 'object_name': 'ParentCategory'},
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
        u'auto_content.extractedarticle': {
            'ArticleImage': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
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
            'TweetImage': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'TweetText': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isLive': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'story_arc.storyarc': {
            'ChildArticles': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['articles.Article']", 'null': 'True', 'blank': 'True'}),
            'ChildStories': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['auto_content.ExtractedArticle']", 'null': 'True', 'blank': 'True'}),
            'DraftTime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'FeaturedProducts': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['articles.FeaturedProduct']", 'symmetrical': 'False'}),
            'Meta': {'ordering': "['-DraftTime']", 'object_name': 'StoryArc'},
            'ParentCategory': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['articles.ParentCategory']"}),
            'PublishTime': ('django.db.models.fields.DateTimeField', [], {}),
            'StoryAuthor': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'StoryDescription': ('django.db.models.fields.TextField', [], {'default': 'None', 'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'StoryMedia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['articles.ArticleMedia']"}),
            'StorySlug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'StorySubtitle': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'StoryText': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'StoryTitle': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isFeatured': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['story_arc']