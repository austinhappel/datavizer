# from django.http import HttpResponse
# from django.shortcuts import get_object_or_404, render
from apps.user_management.utils import get_user_info_from_session_key
# from django.template import RequestContext


def get_user_info(fn):
    """decorator used to get the user's info. If no sessionkey exists,
    this decorator will pass userInfo=None as a kwarg to the receiver."""
    def wrapper(request, **kwargs):
        if 'userInfo' in kwargs:
            return fn(request, **kwargs)

        if request.session.session_key is None:
            kwargs['userInfo'] = None
            return fn(request, **kwargs)

        kwargs['userInfo'] = get_user_info_from_session_key(request.session.session_key)
        return fn(request, **kwargs)

    return wrapper
