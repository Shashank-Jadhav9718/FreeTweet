"""
Django settings for freetweet project.
"""

from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-lqg#1*p+412e1=yg7($+4!#%3e(_t5yn)308q56h9ywpqwn7q#'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tweet', # Your app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'freetweet.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Correctly point to your project-level templates directory
        'DIRS': [BASE_DIR / 'templates'], 
        'APP_DIRS': True, # Also look for templates inside apps
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'freetweet.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True # Corrected typo here
USE_TZ = True

STATIC_URL = 'static/'
# Ensure this points to a 'static' folder directly inside your BASE_DIR
STATICFILES_DIRS = [BASE_DIR / 'static'] 

MEDIA_URL = '/media/'
# Ensure this points to a 'media' folder directly inside your BASE_DIR
MEDIA_ROOT = BASE_DIR / 'media' 

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --- AUTHENTICATION URLS ---
# This tells Django where to redirect users if @login_required blocks them.
# It should be the *name* of your custom login URL pattern from freetweet/urls.py
LOGIN_URL = 'login' 

# This tells Django where to redirect users AFTER successful login.
# '/' points to your homepage (tweet_list_root).
LOGIN_REDIRECT_URL = '/' 

# This tells Django where to redirect users AFTER logout (from anywhere, incl. admin).
# '/' points to your homepage (tweet_list_root).
LOGOUT_REDIRECT_URL = '/'

