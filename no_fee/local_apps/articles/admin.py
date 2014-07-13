from django.contrib import admin
from models import Category, SlideshowBanner, FeaturedArticle, FeaturedProduct, ArticleMedia, Article

class FeaturedProductInline(admin.TabularInline):
	model = FeaturedProduct

class FeaturedArticleinline(admin.TabularInline):
	model = FeaturedArticle

class ArticleMediaInline(admin.TabularInline):
	model = ArticleMedia
		
class ArticleAdmin(admin.ModelAdmin):
	model = Article
	change_form_template = 'articles_change_form.html'
	inline = [
		FeaturedProductInline,
		FeaturedArticleinline,
		ArticleMediaInline,
	]

admin.site.register(Category)
# admin.site.register(SubCategory)
admin.site.register(SlideshowBanner)
admin.site.register(ArticleMedia)
admin.site.register(FeaturedProduct)
admin.site.register(FeaturedArticle)
admin.site.register(Article, ArticleAdmin)
