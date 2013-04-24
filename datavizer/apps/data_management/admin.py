from django.contrib import admin
from apps.data_management.models import Datum, DataType


class DatumAdmin(admin.ModelAdmin):
    fields = ['datatype', 'owner', 'data']


class DataTypeAdmin(admin.ModelAdmin):
    fields = ['name', 'owner']


admin.site.register(DataType, DataTypeAdmin)
admin.site.register(Datum, DatumAdmin)
