from django import forms
from data_fields import data_fields_form_choices
from .models import DataType, DataSet, Datum
from django.forms import ModelForm
# from django.forms.models import inlineformset_factory
from django.core.validators import validate_slug
from apps.user_management.utils import user_from_session_key


class AddDatumForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(AddDatumForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Datum
        exclude = ('owner', )


class DataSetForm(ModelForm):

    def __init__(self, user, *args, **kwargs):
        super(DataSetForm, self).__init__(*args, **kwargs)
        self.fields['datatype'] = forms.ModelChoiceField(queryset=DataType.objects.filter(owner=user))
        self.fields['name'].label = 'Name / Unique identifier'

    class Meta:
        model = DataSet
        exclude = ('owner', )


class CreateNewDataType(forms.Form):
    fields = forms.ChoiceField(data_fields_form_choices)


class CreateNewDataTypeAddField(forms.Form):
    name = forms.CharField(max_length=1024, validators=[validate_slug])
    field = forms.ChoiceField(data_fields_form_choices)


class DataTypeForm(ModelForm):
    class Meta:
        model = DataType
        exclude = ('owner', )

    def clean_schema(self):
        data = self.cleaned_data['schema']
        for fieldName in data:
            valid = False

            # ensure the field name is alphanumeric
            validate_slug(fieldName)

            for fieldType, name in data_fields_form_choices:
                if fieldType == data[fieldName]:
                    valid = True

            if valid is False:
                return ValueError('We do not support a field type of: %s', data[fieldName])

        return data
