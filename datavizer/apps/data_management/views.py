# from django.http import HttpResponse
from django.shortcuts import render  # get_object_or_404
from django.template import RequestContext
from apps.user_management.view_decorators import get_user_info
from django.contrib.auth.decorators import login_required
from forms import DataTypeForm
from data_fields import data_fields_form_choices


@get_user_info
@login_required
def create_datatype(request, userInfo=None):
    templateVars = {
        'form_datatype': DataTypeForm(),
        'create_datatype_field_options': data_fields_form_choices,
        'userInfo': userInfo,
    }

    context = RequestContext(request, templateVars)

    return render(request, 'data_management/page_create_datatype.html', context)
