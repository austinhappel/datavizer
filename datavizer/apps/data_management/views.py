# from django.http import HttpResponse
from django.shortcuts import render  # get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from apps.user_management.view_decorators import get_user_info
from apps.user_management.utils import user_from_session_key
from django.contrib.auth.decorators import login_required
from forms import DataTypeForm, DataSetForm, AddDatumForm
from data_fields import data_fields_form_choices
from .models import DataType, DataSet, Datum
from django.db import IntegrityError
import json


@get_user_info
@login_required
def import_data(request, userInfo=None):
    pass


@get_user_info
@login_required
def import_datum(request, userInfo=None):

    responseData = {
        'res': 'err',
        'error': 'not implemented yet.'
    }

    return HttpResponse(json.dumps(responseData), mimetype="application/json")


@login_required
def get_dataset_schema(request, userInfo=None, id=None):
    user = user_from_session_key(request.session.session_key)

    if request.method == 'GET':
        try:
            target_dataset = DataSet.objects.filter(owner=user).get(pk=int(id))

            responseData = {
                'res': 'ok',
                'schema': target_dataset.datatype.schema
            }
        except ObjectDoesNotExist:
            responseData = {'res': 'err'}

    return HttpResponse(json.dumps(responseData), mimetype="application/json")


@get_user_info
@login_required
def add_data(request, userInfo=None):
    errors = None
    save_success = None
    user = user_from_session_key(request.session.session_key)

    if request.method == 'POST':
        form = AddDatumForm(user, request.POST)

        if form.is_valid():

            newDatum = Datum(
                dataset=form.cleaned_data['dataset'],
                data=form.cleaned_data['data'],
                owner=user
            )

            newDatum.save()

        else:
            errors = form.errors

    templateVars = {
        'form_datum': AddDatumForm(user),
        'form_datum_fields': {},
        'userInfo': userInfo,
        'errors': errors,
        'save_success': save_success,
        'activePage': 'add_data'
    }

    context = RequestContext(request, templateVars)

    return render(request, 'data_management/page_add_data.html', context)


@get_user_info
@login_required
def create_dataset(request, userInfo=None):
    errors = None
    save_success = None
    user = user_from_session_key(request.session.session_key)
    title = "Create Dataset"

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
        'activePage': 'create_dataset',
        'title': title
    }

    context = RequestContext(request, templateVars)

    return render(request, 'data_management/page_create_edit_dataset.html', context)


@get_user_info
@login_required
def edit_dataset(request, userInfo=None, username=None, dataset_id=None):
        errors = None
        save_success = None
        user = user_from_session_key(request.session.session_key)

        if request.method == 'GET':
            dataset = DataSet.objects.filter(id=dataset_id, owner=user)
            title = "Edit Dataset: %s" % dataset[0].name

            # if we don't have a dataset of that name, throw a 404
            if len(dataset) == 0:
                templateVars = {
                    'userInfo': userInfo
                }

                context = RequestContext(request, templateVars)
                return render(request, 'pages/error_404.html', context)

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

        print dir(userInfo)
        templateVars = {
            'form_dataset': DataSetForm(user),
            'userInfo': userInfo,
            'errors': errors,
            'save_success': save_success,
            'activePage': 'create_dataset',
            'title': title
        }

        context = RequestContext(request, templateVars)

        return render(request, 'data_management/page_create_edit_dataset.html', context)


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
