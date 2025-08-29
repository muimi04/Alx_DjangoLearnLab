# settings/production.py
from .base import *   # your common settings
import os
from pathlib import Path
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = False
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']  # required

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "").split(",")  # e.g. "example.com,app.herokuapp.com"

# Security
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = os.environ.get("DJANGO_SECURE_SSL_REDIRECT", "True") == "True"

# Static & media (change if using S3)
STATIC_ROOT = BASE_DIR / "staticfiles"
MEDIA_ROOT = BASE_DIR / "mediafiles"
STATIC_URL = "/static/"
MEDIA_URL = "/media/"

# Database (expects DATABASE_URL env var)
DATABASES = {"default": dj_database_url.parse(os.environ['DATABASE_URL'])}

# REST Framework production settings
REST_FRAMEWORK['DEFAULT_PAGINATION_CLASS'] = 'rest_framework.pagination.PageNumberPagination'
REST_FRAMEWORK['PAGE_SIZE'] = int(os.environ.get('PAGE_SIZE', 20))
