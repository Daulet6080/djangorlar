import os
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR=Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR/ '.env')

ENV_ID = os.getenv("DJANGORLAR_ENV_ID","local")

if ENV_ID == "local":
    DEBUG =True
    ALLOWED_HOSTS=[]
else:
    DEBUG=False
    ALLOWED_HOSTS = ["Dauletskiy.com"]
    