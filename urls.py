#from django.conf.urls.defaults import *
from django.conf.urls import patterns, include, url
from demo import settings
#from django.conf import settings
from demo.feed import LastestEntries

from django.contrib import admin
admin.autodiscover()

feeds = {
		'lastest':LastestEntries,
		}

urlpatterns = patterns('',
    # Example:
    # (r'^demo/', include('demo.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #(r'^blog/', include('demo.blog.urls')),
    #(r'^test/(?P<art_id>\d+)/$','demo.blog.views.detail'),
    
    #(r'^admin/(.*)', admin.site.root),
    url(r'^admin/', include(admin.site.urls)),

    (r'^search/?$','demo.blog.views.search'),
    (r'^blog/','demo.blog.views.index'),
    (r'^article/(?P<art_id>\d+)/$','demo.blog.views.detail'),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.STATIC_PATH}),
    #(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':'./mymedia'}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':'./template'}),
    #(r'^feeds/(?P<url>.*)/$','django.contrib.syndication.views.feed',{'feed_dict':feeds}),
    (r'^page/(?P<page_id>\d+)/$','demo.blog.views.page'),
    (r'^cate/(?P<cate_id>\d+)/$','demo.blog.views.cate'),
    (r'^microblog/(?P<p_id>\d+)/$','demo.microblog.views.index'),
    (r'^send/?$','demo.microblog.views.send'),
    (r'^sendcomment/(?P<art_id>\d+)/$','demo.blog.views.sendcomment'),
    #(r'^tinymce/', include('tinymce.urls')),
)
