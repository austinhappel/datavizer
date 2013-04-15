from django.conf.urls import patterns, include, url
from django.contrib import admin
# from django.views.generic.simple import direct_to_template

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'datavizer.views.home', name='home'),
    # url(r'^datavizer/', include('datavizer.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^admin/', include('django.contrib.admin.urls')),
    (r'^accounts/', include('registration.urls')),

    # catch-all for pages
    (r'^$', include('apps.pages.urls')),
    (r'^/$', include('apps.pages.urls')),
)
