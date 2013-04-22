from django.db import models
# from apps.data_management.json_field import JSONField
from jsonfield import JSONField
from django.contrib.auth.models import User


# text, integer, float, date
class DataField(models.Model):
    """
    An individual field in a datatype. These are hard-coded(?) fields that have
    specific validation requirements. A datatype is comprised of a list of
    these datafields.
    """
    name = models.CharField(max_length=255)
    optional = models.BooleanField()  # whether or not this field should be required when adding new data to the system.

    def __unicode__(self):
        return u'%s' % self.name


class Datum(models.Model):
    """
    Individual piece of data. Each piece of data has a data type associated
    with it, which will govern how this piece of data is validated.
    """
    date_added = models.DateTimeField(auto_now_add=True)
    datatype = models.ForeignKey('DataType')
    owner = models.ForeignKey(User)
    data = JSONField()

    def __unicode__(self):
        return u'datum of type %s created on %s' % (self.datatype, self.date_added)

    class Meta:
        verbose_name_plural = "data"


class DataType(models.Model):
    """
    A schema for new data. Every Datum that is added has a DataType associated
    with it, and the schema of that datum must match the schema dictated in
    it's datatype.
    """
    date_added = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User)
    fields = models.ManyToManyField(DataField)

    def __unicode__(self):
        return u'%s' % self.name
