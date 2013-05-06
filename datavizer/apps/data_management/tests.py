"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from forms import DataTypeForm


class DataTypeFormTestCase(TestCase):
    def test_bad_schema(self):
        """
        Tests bad schema being passed as values for the datatype fields.
        """
        datatype = DataTypeForm({
            u'name': u'faaa',
            u'schema': u'{"sdf":"buttField"}'
        })

        self.assertEquals(False, datatype.is_valid())

    def test_bad_field_name(self):
        """
        Tests that the form is invalid if a field name is not alphanumeric.
        """
        datatype = DataTypeForm({
            u'name': u'faaa',
            u'schema': u'{"what!":"textField"}'
        })

        self.assertEquals(False, datatype.is_valid())

    def test_bad_form_title(self):
        """
        Tests that the form is invalid if the datatype name is not alphanumeric.
        """
        datatype = DataTypeForm({
            u'name': u'faaa!',
            u'schema': u'{"what":"textField"}'
        })

        self.assertEquals(False, datatype.is_valid())
