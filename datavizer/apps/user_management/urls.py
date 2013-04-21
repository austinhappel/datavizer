from django.conf.urls import patterns, include, url

# (?P<name>pattern)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'datavizer.views.home', name='home'),
    # url(r'^datavizer/', include('datavizer.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^/?$', 'apps.user_management.views.user_account', name='user_account'),
    url(r'^(?P<username>[a-zA-Z0-9_\-]*)/$', 'apps.user_management.views.user_account', name='user_account'),
)
