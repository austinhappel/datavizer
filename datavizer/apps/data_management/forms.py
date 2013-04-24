from django import forms
from data_fields import data_fields_form_choices


class CreateNewDataType(forms.Form):
    fields = forms.ChoiceField(data_fields_form_choices)
