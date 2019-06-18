from .hideheroku import *

import dj_database_url

# SECURITY WARNING: don't run with debug turned on in production!
#if os.environ.get('debug', False):
    # SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
#else:
   # DEBUG = False

ALLOWED_HOSTS = ['*']
DATABASES['default'] = dj_database_url.config()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'blog',
    'cloudinary',
    'cloudinary_storage',
]
