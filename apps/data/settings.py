from config.settings import *

ROOT_URLCONF = 'apps.data.urls'
WSGI_APPLICATION = 'apps.data.wsgi.application'

try:
    from .local_settings import *
except:
    pass