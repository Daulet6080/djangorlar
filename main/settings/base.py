from pathlib import Path
from decouple import config,Csv

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY =config("SECRET_KEY",default="unsafe-secret")
DEBUG=config("DEBUG",default=False,cast=bool)
ALLOWED_HOSTS=config('ALLOWED_HOSTS',default="",cast=Csv())
