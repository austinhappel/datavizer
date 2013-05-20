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
    (r'^accounts/', include('registration.backends.default.urls')),

    # user account views
    (r'^user/', include('apps.user_management.urls')),

    # data views
    (r'^data/', include('apps.data_management.urls')),

    # pages urls
    # home
    url(r'^/?$', 'apps.pages.views.index', name='index'),
    # about
    url(r'^about/?$', 'apps.pages.views.about', name='about'),

    # browse
    url(r'^browse/?$', 'apps.pages.views.browse', name='browse'),

    # oauth2
    url(r'^oauth2/', include('provider.oauth2.urls', namespace='oauth2'))
)

handler404 = 'apps.pages.views.error_404'
handler500 = 'apps.pages.views.error_500'
