from django.conf.urls import patterns, include, url
from django.contrib import admin

from perfis.views import index

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'connectedin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('perfis.urls')),
    url(r'^', include('usuarios.urls')),
)
