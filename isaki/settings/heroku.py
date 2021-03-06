from .common import *

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

CLOUDINARY_STORAGE = {
'CLOUD_NAME': os.environ['CLOUDINARY_CLOUD_NAME'],
'API_KEY': os.environ['CLOUDINARY_API_KEY'],
'API_SECRET': os.environ['CLOUDINARY_API_SECRET']
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

