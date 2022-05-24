from config.settings import *

ROOT_URLCONF = 'apps.site.urls'
WSGI_APPLICATION = 'apps.site.wsgi.application'

try:
    from .local_settings import *
except:
    pass