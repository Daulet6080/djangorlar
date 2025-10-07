# Project modules
from settings.base import *

SECRET_KEY = "django-insecure-5h7&1u#2_p+0z1q8y@l-r!x#y8!a7m5b2f9%l93kd4f8g@u$"
# ↑ можешь использовать этот ключ или сгенерировать свой

DEBUG = True
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    },
}
