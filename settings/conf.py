import os
from decouple import config

ENV_POSSIBLE_OPTIONS = ["local", "prod"]

# читаем из .env
ENV_ID = config("DJANGORLAR_ENV_ID", default="local")

if ENV_ID not in ENV_POSSIBLE_OPTIONS:
    raise ValueError(f"Invalid DJANGORLAR_ENV_ID: {ENV_ID}")

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # твои приложения
    'abstracts',
]
