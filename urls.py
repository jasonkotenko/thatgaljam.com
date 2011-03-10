from django.conf.urls.defaults import *
from django.contrib import admin
from thatgaljam import settings


admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'thatgaljam.posts.views.latest'),
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
