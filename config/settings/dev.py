from pathlib import Path
from decouple import config, Csv
from .base import *

DEBUG = config("DEBUG", cast=bool, default=True)
ALLOWED_HOSTS += ["127.0.0.1", "localhost"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),

    }
}
