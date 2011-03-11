from django.contrib import admin
from models import Article

class ArticleAdmin(admin.ModelAdmin):
  class Media:
    js = ('/media/js/tiny_mce/tiny_mce.js',
      '/media/js/tiny_mce/textareas.js',)

admin.site.register(Article, ArticleAdmin)