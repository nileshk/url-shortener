from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns(
    '',
    (r'^$', 'shortener.views.index'),    
    (r'^admin/(.*)', admin.site.root),    
    (r'^submit/$', 'shortener.views.submit'),
    (r'^(?P<base62_id>\w+)$', 'shortener.views.follow'),
    (r'^info/(?P<base62_id>\w+)$', 'shortener.views.info'),    

    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
      {'document_root': settings.STATIC_DOC_ROOT}),
)
