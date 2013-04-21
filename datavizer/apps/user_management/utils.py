from django.contrib.sessions.models import Session
from django.contrib.auth.models import User


def get_user_info_from_session_key(session_key):

    session = Session.objects.get(session_key=session_key)
    uid = session.get_decoded().get('_auth_user_id')
    user = User.objects.get(pk=uid)

    return {
        'username': user.username,
        'full_name': user.get_full_name(),
        'email': user.email
    }
