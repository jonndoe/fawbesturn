from .base import *  # noqa: F403, F401
import os



ALLOWED_HOSTS = ['80.78.254.210','localhost', 'www.moreforum.ru', 'www.drivedex.ru', 'drivedex.ru',]

DEBUG = os.getenv('DJANGO_DEBUG', 'off') == 'on'

# CACHING IN PRODUCTION
CACHE_MIDDLEWARE_ALIAS = 'default'
CACHE_MIDDLEWARE_SECONDS = 604800
CACHE_MIDDLEWARE_KEY_PREFIX = ''

SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'SAMEORIGIN'
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 3600 
SECURE_HSTS_INCLUDE_SUBDOMAINS = True 
SECURE_HSTS_PRELOAD = True 
SECURE_CONTENT_TYPE_NOSNIFF = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_REFERRER_POLICY = 'same-origin'


EMAIL_BACKEND = os.getenv('EMAIL_BACKEND')
print('Email Backend', EMAIL_BACKEND)

EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS')

SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DATABASE_NAME'),
        'USER': os.getenv('DATABASE_USER'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '',
        }
}
'''