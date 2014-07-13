from django.contrib import admin
from models import ExtractedArticle

# Register your models here.

class ExtractedArticleAdmin(admin.ModelAdmin):
	model = ExtractedArticle
	change_form_template = 'articles_change_form.html'

admin.site.register(ExtractedArticle, ExtractedArticleAdmin)
