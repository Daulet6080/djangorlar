import os
from decouple import config

ENV_POSSIBLE_OPTIONS = ["local", "prod"]

# читаем из .env
ENV_ID = config("DJANGORLAR_ENV_ID", default="local")

if ENV_ID not in ENV_POSSIBLE_OPTIONS:
    raise ValueError(f"Invalid DJANGORLAR_ENV_ID: {ENV_ID}")
