from django.conf.urls import patterns, include, url

# (?P<name>pattern)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'datavizer.views.home', name='home'),
    # url(r'^datavizer/', include('datavizer.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^create_datatype/$', 'apps.data_management.views.create_datatype', name='create_datatype'),
)
