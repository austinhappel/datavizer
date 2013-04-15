from ..settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'datavizer',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'austin',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# Django Registration

ACCOUNT_ACTIVATION_DAYS = os.getenv('DJ_REG_ACCOUNT_ACTIVATION_DAYS', 7)
EMAIL_HOST = os.getenv('DJ_REG_EMAIL_HOST', 'localhost')
EMAIL_PORT = os.getenv('DJ_REG_EMAIL_PORT', '1025')
EMAIL_USE_TLS = False
EMAIL_HOST_USER = os.getenv('DJ_REG_EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.getenv('DJ_REG_EMAIL_HOST_PASSWORD', '')

# django-compressor

COMPRESS_ENABLED = False
