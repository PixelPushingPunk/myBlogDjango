from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myBlog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # Homepage
    url(r'^$', 'blogs.views.home', name='home'),
    url(r'^blog/(?P<id>[\d]+)/$', 'blogs.views.home', name='blog single'),

    # Forms
    url(r'^forms/', 'blogs.views.home_forms', name='home forms'),


    # Not pages
    # --------------------------------------------------------------------------------------------------

    # Ckeditor
    url(r'^ckeditor/', include('ckeditor.urls')),

    # Media
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

    # All Auth
    url(r'^accounts/', include('allauth.urls')),

    #Admin
    url(r'^admin/', include(admin.site.urls)),
)
