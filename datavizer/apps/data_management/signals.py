from django.dispatch import receiver
from registration.signals import user_activated  # user_registered,
from provider.oauth2.models import Client
from conf import settings


@receiver(user_activated)
def check_activated(sender, user, request, **kwarg):
    if len(Client.objects.filter(user_id=user.id)) < 1:
        c = Client(user=user, name=user.username, client_type=1, url=settings.SITE_URL)
        c.save()
