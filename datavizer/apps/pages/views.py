from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import RequestContext


def index(request):
    print request.session.keys()

    tempVars = {}

    if request.session.get('_auth_user_id') is not None:
        tempVars['is_logged_in'] = True
        tempVars['user_name'] = 'TODO: Add a user here!'

    context = RequestContext(request, tempVars)
    return render(request, 'pages/index.html', context)
