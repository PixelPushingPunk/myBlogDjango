from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myBlog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'blogs.views.home', name='home'),
    url(r'^ckeditor/', include('ckeditor.urls')),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

    url(r'^admin/', include(admin.site.urls)),
)
