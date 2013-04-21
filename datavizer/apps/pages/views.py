# from django.http import HttpResponse
from django.shortcuts import render  # get_object_or_404
from django.template import RequestContext
from apps.user_management.view_decorators import get_user_info


@get_user_info
def index(request, userInfo=None):
    templateVars = {
        'userInfo': userInfo
    }

    context = RequestContext(request, templateVars)
    return render(request, 'pages/index.html', context)


@get_user_info
def about(request, userInfo=None):
    templateVars = {
        'userInfo': userInfo
    }
    context = RequestContext(request, templateVars)
    return render(request, 'pages/about.html', context)


@get_user_info
def browse(request, userInfo=None):
    templateVars = {
        'userInfo': userInfo
    }
    context = RequestContext(request, templateVars)
    return render(request, 'pages/browse.html', context)


@get_user_info
def error_404(request, userInfo=None):
    templateVars = {
        'userInfo': userInfo
    }
    context = RequestContext(request, templateVars)
    return render(request, 'pages/error_404.html', context)


@get_user_info
def error_500(request, userInfo=None):
    templateVars = {
        'userInfo': userInfo
    }
    context = RequestContext(request, templateVars)
    return render(request, 'pages/error_500.html', context)
