from tastypie.resources import ModelResource
from .models import Datum
from authentication import OAuth20Authentication
from tastypie.authorization import DjangoAuthorization
# from tastypie import fields


class DatumResource(ModelResource):
    class Meta:
        queryset = Datum.objects.all()
        resource_name = 'data'
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
