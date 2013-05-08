from django.conf.urls import patterns, include, url

# (?P<name>pattern)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'datavizer.views.home', name='home'),
    # url(r'^datavizer/', include('datavizer.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # forms
    url(r'^create_datatype/$', 'apps.data_management.views.create_datatype', name='create_datatype'),
    url(r'^create_dataset/$', 'apps.data_management.views.create_dataset', name='create_dataset'),
    url(r'^add_data/$', 'apps.data_management.views.add_data', name='add_data'),

    # api
    url(r'^import_datum/$', 'apps.data_management.views.import_datum', name='import_datum'),
    url(r'^import_data/$', 'apps.data_management.views.import_data', name='import_data'),
    url(r'^get_dataset_schema/(?P<id>\d+)/$', 'apps.data_management.views.get_dataset_schema', name='get_dataset_schema'),
)
