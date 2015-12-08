"""Default settings for the ``server_guardian_api`` app."""
from django.conf import settings


PROCESSORS = getattr(
    settings,
    'SERVER_GUARDIAN_PROCESSORS',
    [
        ('dummy', 'server_guardian_api.processors.dummy_processor')
    ]
)

SECURITY_TOKEN = settings.SERVER_GUARDIAN_SECURITY_TOKEN