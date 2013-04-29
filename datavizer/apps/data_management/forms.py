from django import forms
from data_fields import data_fields_form_choices
from .models import DataType  # , Datum, DataSet
from django.forms import ModelForm
# from django.forms.models import inlineformset_factory


class CreateNewDataType(forms.Form):
    fields = forms.ChoiceField(data_fields_form_choices)


class CreateNewDataTypeAddField(forms.Form):
    name = forms.CharField(max_length=1024)
    field = forms.ChoiceField(data_fields_form_choices)


class DataTypeForm(ModelForm):
    class Meta:
        model = DataType
        exclude = ('owner', )
