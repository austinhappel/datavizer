# from django.http import HttpResponse
from django.shortcuts import render  # get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.utils.safestring import SafeString
from apps.user_management.view_decorators import get_user_info
from apps.user_management.utils import user_from_session_key
from django.contrib.auth.decorators import login_required
from forms import DataTypeForm, DataSetForm, AddDatumForm, VisualizationForm
from constants import data_fields_form_choices
from .models import DataType, DataSet, Datum, Visualization
from django.db import IntegrityError
import json


@get_user_info
@login_required
def line_graph(request, userInfo=None):
    errors = None
    save_success = None
    user = user_from_session_key(request.session.session_key)

    dataset_options = DataSet.objects.filter(owner=user).values('id', 'name');

    if request.method == 'POST':

        form = VisualizationForm(user, request.POST)
        if form.is_valid():

            newVisualization = Visualization(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                visualization_type=form.cleaned_data['visualization_type'],
                owner=user,
                legends=form.cleaned_data['legends'],
                is_public=form.cleaned_data['is_public'],
            )

            try:
                newVisualization.save()
                save_success = True
            except IntegrityError:
                errorText = [u'You already have a dataset of \
this same name. Please change the name or edit the other dataset of the same name.']
                if hasattr(form._errors, 'title'):
                    form._errors['title'].push(form.error_class(errorText))
                else:
                    form._errors['title'] = form.error_class(errorText)

                errors = form.errors

        else:
            errors = form.errors

    templateVars = {
        'form_visualization': VisualizationForm(user),
        'userInfo': userInfo,
        'errors': errors,
        'save_success': save_success,
        'activePage': 'create_visualization',
        'dataset_options': json.dumps(list(dataset_options))
    }

    context = RequestContext(request, templateVars)

    return render(request, 'data_management/visualization_forms/page_line_graph_form.html', context)
