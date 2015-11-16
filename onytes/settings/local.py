import os
from onytes.settings.base import *

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, os.path.pardir, 'db.sqlite3.local')
    }
}


MEDIA_ROOT = os.path.join(BASE_DIR, os.path.pardir, os.path.pardir, 'media')
MEDIA_URL = 'media/'

if not os.path.exists(MEDIA_ROOT):
    os.makedirs(MEDIA_ROOT)
