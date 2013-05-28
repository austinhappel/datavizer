# from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from apps.user_management.utils import get_user_info_from_session_key, user_from_session_key
from apps.user_management.view_decorators import get_user_info
from django.template import RequestContext
from apps.data_management.models import Datum, DataType, DataSet
from provider.oauth2.models import Client


def check_user_access(fn):
    """decorator used to ensure that the user has access to the page they're trying to access."""
    def wrapper(request, **kwargs):
        if request.session.session_key is None:
            return error_not_logged_in(request)

        # if we get this far, sessionkey exists.
        userInfo = get_user_info_from_session_key(request.session.session_key)

        if 'username' in kwargs:
            if userInfo['username'] != kwargs['username']:
                return error_not_logged_in(request, **kwargs)

        # username does not exist, meaning we should just pass the
        # request through to the view, but add 'userInfo' to the kwargs.
        if 'userInfo' not in kwargs:
            kwargs['userInfo'] = userInfo

        return fn(request, **kwargs)

    return wrapper


@check_user_access
def user_account(request, username=None, userInfo=None):
    """Display the user account. Since this is decorated with checkUserAccess,
    we can assume that a sessionKey always will exist."""

    user = user_from_session_key(request.session.session_key)
    oauth2Client = Client.objects.filter(user=user)

    if userInfo is None:
        userInfo = get_user_info_from_session_key(request.session.session_key)

    if oauth2Client is not None and len(oauth2Client) > 0:
        oauth2ClientId = oauth2Client[0].client_id
        oauth2ClientSecret = oauth2Client[0].client_secret

    templateVars = {
        'userInfo': userInfo,
        'activePage': 'account',
        'your_datasets': DataSet.objects.filter(owner=user),
        'your_datatypes': DataType.objects.filter(owner=user),
        'your_visualizations': None,
        'latest_data': Datum.objects.filter(owner=user).order_by('date_added')[:10],
        'oauth2ClientId': oauth2ClientId,
        'oauth2ClientSecret': oauth2ClientSecret
    }

    context = RequestContext(request, templateVars)
    return render(request, 'user_management/user_account.html', context)


@get_user_info
def error_not_logged_in(request, userInfo=None):
    templateVars = {
        'userInfo': userInfo
    }
    context = RequestContext(request, templateVars)
    return render(request, 'pages/error_not_logged_in.html', context)
