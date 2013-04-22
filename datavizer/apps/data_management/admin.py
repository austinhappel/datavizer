from django.contrib import admin
from apps.data_management.models import DataField, Datum, DataType


class DataFieldAdmin(admin.ModelAdmin):
    fields = ['name', 'optional']


class DatumAdmin(admin.ModelAdmin):
    fields = ['datatype', 'owner', 'data']


class DataTypeAdmin(admin.ModelAdmin):
    fields = ['name', 'owner', 'fields']


admin.site.register(DataField, DataFieldAdmin)
admin.site.register(DataType, DataTypeAdmin)
admin.site.register(Datum, DatumAdmin)
