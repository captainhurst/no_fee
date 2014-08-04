from django.contrib import admin
from models import Category, FeaturedArticle, ArticleMedia, Article

class FeaturedArticleinline(admin.TabularInline):
	model = FeaturedArticle

class ArticleMediaInline(admin.TabularInline):
	model = ArticleMedia
		
class ArticleAdmin(admin.ModelAdmin):
	model = Article
	change_form_template = 'articles_change_form.html'
	inline = [
		FeaturedArticleinline,
		ArticleMediaInline,
	]

admin.site.register(Category)
# admin.site.register(SubCategory)
admin.site.register(ArticleMedia)
admin.site.register(FeaturedArticle)
admin.site.register(Article, ArticleAdmin)
