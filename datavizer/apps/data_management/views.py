# from django.http import HttpResponse
from django.shortcuts import render  # get_object_or_404
from django.template import RequestContext
from apps.user_management.view_decorators import get_user_info
from apps.user_management.utils import user_from_session_key
from django.contrib.auth.decorators import login_required
from forms import DataTypeForm, DataSetForm
from data_fields import data_fields_form_choices
from .models import DataType, DataSet
from django.db import IntegrityError


@get_user_info
@login_required
def create_dataset(request, userInfo=None):
    errors = None
    save_success = None
    user = user_from_session_key(request.session.session_key)

    if request.method == 'POST':

        form = DataSetForm(user, request.POST)
        if form.is_valid():

            newDataSet = DataSet(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                datatype=form.cleaned_data['datatype'],
                owner=user
            )

            try:
                newDataSet.save()
                save_success = True
            except IntegrityError:
                errorText = [u'You already have a dataset of \
this same name. Please change the name or edit the other dataset of the same name.']
                if hasattr(form._errors, 'name'):
                    form._errors['name'].push(form.error_class(errorText))
                else:
                    form._errors['name'] = form.error_class(errorText)

                errors = form.errors

        else:
            errors = form.errors

    templateVars = {
        'form_dataset': DataSetForm(user),
        'userInfo': userInfo,
        'errors': errors,
        'save_success': save_success,
        'activePage': 'create_dataset'
    }

    context = RequestContext(request, templateVars)

    return render(request, 'data_management/page_create_dataset.html', context)


@get_user_info
@login_required
def create_datatype(request, userInfo=None):
    errors = None
    save_success = None

    if request.method == 'POST':
        form = DataTypeForm(request.POST)
        if form.is_valid():
            user = user_from_session_key(request.session.session_key)

            newDataType = DataType(
                name=form.cleaned_data['name'],
                schema=form.cleaned_data['schema'],
                owner=user
            )

            try:
                newDataType.save()
                save_success = True
            except IntegrityError:
                errorText = [u'You already have a datatype of \
this same name. Please change the name or edit the other datatype of the same name.']
                if hasattr(form._errors, 'name'):
                    form._errors['name'].push(form.error_class(errorText))
                else:
                    form._errors['name'] = form.error_class(errorText)

                errors = form.errors

        else:
            errors = form.errors

    templateVars = {
        'form_datatype': DataTypeForm(),
        'create_datatype_field_options': data_fields_form_choices,
        'userInfo': userInfo,
        'errors': errors,
        'save_success': save_success,
        'activePage': 'create_datatype'
    }

    context = RequestContext(request, templateVars)

    return render(request, 'data_management/page_create_datatype.html', context)
