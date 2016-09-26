from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bird.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url(r'^birds/$', 'api.views.birds', name='birds'),
    url(r'^birds/(?P<bid>\w+)/$', 'api.views.birds', name='birds'),
)
