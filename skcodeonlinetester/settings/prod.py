"""
Production Django settings for the SkCodeOnlineTester project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/

For the full list of common settings and their values, see
``skcodeonlinetester.settings.common.py``
"""

from .common import *

# region ----- Core settings

# Before going on production:
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# Set to true to enable project debug mode
# SECURITY WARNING: don't run with debug turned on in production!
# See https://docs.djangoproject.com/en/1.7/ref/settings/#debug
DEBUG = False

# Set to true to enable template debug mode
# See https://docs.djangoproject.com/en/1.7/ref/settings/#template-debug
TEMPLATES[0]['OPTIONS']['debug'] = False

# List of accepted Host header values, must be synced with the web server configuration
# See https://docs.djangoproject.com/en/1.7/ref/settings/#allowed-hosts
ALLOWED_HOSTS = [
    'pyskcode.tamialab.fr',
]

# endregion

# region ----- Cache settings

# Cache backend options
# See https://docs.djangoproject.com/en/1.7/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
        'LOCATION': SECRETS.get('MEMCACHED_HOST', '127.0.0.1:11211'),
        'KEY_PREFIX': CACHE_KEY_PREFIX,
        'BINARY': True,
    }
}

# endregion

# region ----- Email settings

# Email backend for sending email
# See https://docs.djangoproject.com/en/1.7/ref/settings/#std:setting-EMAIL_BACKEND
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# endregion

# region ----- Media and files upload settings

# URL that handles the media served from MEDIA_ROOT.
# It must end in a slash if set to a non-empty value.
# See https://docs.djangoproject.com/en/1.7/ref/settings/#media-url
MEDIA_URL = 'http://pyskcode.tamialab.fr/uploads/'

# endregion

# region ----- Static files upload settings

# The file storage engine to use when collecting static files with the collectstatic management command.
# See https://docs.djangoproject.com/en/1.7/ref/settings/#std:setting-STATICFILES_STORAGE
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

# URL to use when referring to static files located in STATIC_ROOT.
# See https://docs.djangoproject.com/en/1.7/ref/settings/#static-url
STATIC_URL = 'http://pyskcode.tamialab.fr/static/'

# endregion

# region ----- Template settings

# Template settings - use the cached template loader
# See https://docs.djangoproject.com/en/1.8/ref/templates/upgrading/
del TEMPLATES[0]['APP_DIRS']
TEMPLATES[0]['OPTIONS']['loaders'] = [
    ('django.template.loaders.cached.Loader', [
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    ]),
]

# endregion

# region ----- Sessions settings

# Set to true to force client browser to sent the session cookies over HTTPS
# See https://docs.djangoproject.com/en/1.7/ref/settings/#session-cookie-secure
# FIXME Current production server does not provided HTTPS
SESSION_COOKIE_SECURE = False

# endregion

# region ----- CSRF settings

# Set to true to force client browser to sent the cookies over HTTPS
# See https://docs.djangoproject.com/en/1.7/ref/settings/#csrf-cookie-secure
# FIXME Current production server does not provided HTTPS
CSRF_COOKIE_SECURE = False

# endregion

# region ----- Proxy settings

# Allow local reverse proxy to forward HTTPS over the local http connection
# See https://docs.djangoproject.com/fr/1.8/ref/settings/#secure-proxy-ssl-header
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# endregion
