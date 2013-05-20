from django.contrib.sessions.models import Session
from django.contrib.auth.models import User

from django.conf import settings
from django.contrib.auth import SESSION_KEY, BACKEND_SESSION_KEY, load_backend
from django.contrib.auth.models import AnonymousUser


def get_user_info_from_session_key(session_key):

    session = Session.objects.get(session_key=session_key)
    uid = session.get_decoded().get('_auth_user_id')

    if uid is not None:
        user = User.objects.get(pk=uid)

        return {
            'username': user.username,
            'full_name': user.get_full_name(),
            'email': user.email
        }

    return None


def user_from_session_key(session_key):
    session_engine = __import__(settings.SESSION_ENGINE, {}, {}, [''])
    session_wrapper = session_engine.SessionStore(session_key)
    user_id = session_wrapper.get(SESSION_KEY)
    auth_backend = load_backend(session_wrapper.get(BACKEND_SESSION_KEY))

    if user_id and auth_backend:
        return auth_backend.get_user(user_id)
    else:
        return AnonymousUser()
