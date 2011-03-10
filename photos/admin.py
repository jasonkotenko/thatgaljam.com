from django.contrib import admin
from models import Gallery, Photo, Category

class PhotoInline(admin.TabularInline):
  model = Photo

class GalleryAdmin(admin.ModelAdmin):
  inlines = [
    PhotoInline,
  ]
  
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Photo)
admin.site.register(Category)
