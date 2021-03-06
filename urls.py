from django.conf.urls.defaults import *
from django.contrib import admin
from thatgaljam import settings
from thatgaljam.feeds import PostFeed
from django.views.generic.simple import direct_to_template

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'thatgaljam.posts.views.category', {'req_name':'blog'}, name="home"),
    url(r'^posts/feed/$', PostFeed(), name="posts_feed"),
    url(r'^posts/tag/(?P<tag_name>.*)/$', 'thatgaljam.posts.views.tagged_posts', name="tagged_posts"),
    url(r'^posts/(?P<req_name>.*)/$', 'thatgaljam.posts.views.post', name="single_post"),
    url(r'^category/(?P<req_name>.*)/$', 'thatgaljam.posts.views.category', name="category_view"),
    url(r'^articles/(?P<req_name>.*)/$', 'thatgaljam.articles.views.article', name="single_article"),
    url(r'^gallery/(?P<req_name>.*)/$', 'thatgaljam.photos.views.gallery', name="single_photo_gallery"),
    url(r'^photos/(?P<req_name>.*)/$', 'thatgaljam.photos.views.gallery_list', name="photo_gallery_list"),
    url(r'^contact/$', 'thatgaljam.contact.views.contact', name="contact"),
    url(r'^thanks/$', direct_to_template, {'template':'thanks.html'}, name="thanks"),
)

if settings.DEBUG == True:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )

urlpatterns += patterns('',
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
)
