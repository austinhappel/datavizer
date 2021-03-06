from django.db import models
# from apps.data_management.json_field import JSONField
from jsonfield import JSONField
from django.contrib.auth.models import User
from django.core.validators import validate_slug
import signals  # required to bind to signals, do not comment out.


class Visualization(models.Model):
    """
    Visualization of data added to datatypes
    """
    owner = models.ForeignKey(User)
    title = models.CharField(max_length=1024)
    description = models.TextField()
    visualization_type = models.CharField(max_length=255)
    # colors associated with the fields of data.
    """
    {
        legends: [
            {
                name: 'lskjdf',
                dataset: 'dataset id',
                field1: 'name of dataset field',
                field2: 'name of dataset field',
                fieldN: 'name of dataset field',
                color: '#beefed'
            }
        ]
    }
    """
    legends = JSONField()
    is_public = models.BooleanField()
    datasets = models.ManyToManyField('DataSet')

    def __unicode__(self):
        return u'%s' % self.title


class Datum(models.Model):
    """
    Individual piece of data. Each piece of data has a data type associated
    with it, which will govern how this piece of data is validated.
    """
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)
    data = JSONField()
    dataset = models.ForeignKey('DataSet')

    def __unicode__(self):
        return u'datum of type %s created on %s' % (self.dataset, self.date_added)

    class Meta:
        verbose_name_plural = "data"


class DataType(models.Model):
    """
    A schema for new data. Every Datum that is added has a DataType associated
    with it, and the schema of that datum must match the schema dictated in
    it's datatype.
    """
    date_added = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255, validators=[validate_slug])
    owner = models.ForeignKey(User)
    schema = JSONField()

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        unique_together = ('name', 'owner')


class DataSet(models.Model):
    """
    A set of data comprised of multiple points of data (datum)
    """
    name = models.CharField(max_length=2048)
    description = models.TextField()
    owner = models.ForeignKey(User)
    datatype = models.ForeignKey(DataType)

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        unique_together = ('name', 'owner')
