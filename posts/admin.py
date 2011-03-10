from django.contrib import admin
from models import Post

class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('/media/js/tiny_mce/tiny_mce.js', 
                '/media/js/tiny_mce/textareas.js',)

admin.site.register(Post, PostAdmin)
