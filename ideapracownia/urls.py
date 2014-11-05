from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'pages.views.index', name='home'),
    url(r'^galeria/$', 'gallery.views.index', name='galeria'),
    url(r'^galeria/(?P<page_number_text>\d+)/$', 'gallery.views.index', name='galeria'),
    url(r'galeria/zdjecia/(?P<photo_id>\d+)/$', 'gallery.views.single_photo', name='single_photo'),
    url(r'aktualnosci/$', 'articles.views.index', name='article_index'),
    url(r'aktualnosci/strony=(?P<page_number_text>\d+)/$', 'articles.views.index', name='article_index'),
    url(r'aktualnosci/(?P<article_name>\w+)/$', 'articles.views.single_article', name='single_article'),
    url(r'^(?P<requested_tab_name>\w+)/$', 'pages.views.index', name='index'),

)

#Allow media to be served in debug mode
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()