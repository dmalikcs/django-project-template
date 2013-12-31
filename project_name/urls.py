from django.conf.urls import patterns, include, url
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       url(r'^$', '{{ project_name }}.views.home', name='home'),
                       # url(r'^{{ project_name }}/', include('{{ project_name }}.foo.urls')),
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       )
if settings.DEBUG:
    urlpatterns += patterns('', url(r'%s(?P<path>.*)' % settings.MEDIA_URL[1:], 'django.views.static.serve', {'document_root': setti ngs.MEDIA_ROOT}),)
