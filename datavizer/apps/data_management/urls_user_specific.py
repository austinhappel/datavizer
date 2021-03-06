from django.conf.urls import patterns, include, url

# (?P<name>pattern)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'datavizer.views.home', name='home'),
    # url(r'^datavizer/', include('datavizer.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # forms
    url(r'^edit_dataset/(?P<dataset_id>[a-zA-Z0-9_\-]*)/$', 'apps.data_management.views.edit_dataset', name='edit_dataset'),
    url(r'^edit_datatype/(?P<datatype_id>[a-zA-Z0-9_\-]*)/$', 'apps.data_management.views.edit_datatype', name='edit_datatype'),

    # url(r'^create_dataset/$', 'apps.data_management.views.create_dataset', name='create_dataset'),
    # url(r'^add_data/$', 'apps.data_management.views.add_data', name='add_data'),

    # # api
    # url(r'^import_datum/$', 'apps.data_management.views.import_datum', name='import_datum'),
    # url(r'^import_data/$', 'apps.data_management.views.import_data', name='import_data'),
)
