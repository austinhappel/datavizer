from django.conf.urls import patterns, include, url
from tastypie.api import Api
from .api import DatumResource

# (?P<name>pattern)

v1_api = Api(api_name='v1')
v1_api.register(DatumResource())

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

    # visualization forms
    url(r'^visualizations/create/$', 'apps.data_management.views.create_visualization', name='create_visualization'),
    url(r'^visualizations/create/line_graph/$', 'apps.data_management.views_visualization_forms.line_graph', name='line_graph'),


    # api
    url(r'^import_datum/$', 'apps.data_management.views.import_datum', name='import_datum'),
    url(r'^import_data/$', 'apps.data_management.views.import_data', name='import_data'),
    url(r'^get_dataset_schema/(?P<id>\d+)/$', 'apps.data_management.views.get_dataset_schema', name='get_dataset_schema'),

    # tastypie datum api
    url(r'^api/', include(v1_api.urls)),

)
