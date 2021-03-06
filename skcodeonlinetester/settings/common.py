"""
Common Django settings for the SkCodeOnlineTester project.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os    # For filesystem PATH generation and traversing
import json  # For secret configuration file parsing
import warnings

from django.utils.translation import ugettext_lazy as _

# Detect test mode
TESTING = False

# IMPORTANT NOTE: DO NOT USE TUPLE, USE LIST, otherwise dev/prod settings overload will break

# region ----- Root directory path setting

# Root directory of the project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

# endregion

# region ----- Secret settings loading from JSON file

# Catch error to provide fallback in case of debug environment (no secret file)
try:

    # Open the secret settings JSON file and load it's content
    with open(os.path.join(os.path.dirname(BASE_DIR), 'skcodeonlinetester-secrets.json')) as fi_handle:
        SECRETS = json.load(fi_handle)

except IOError:

    # No secret file, try to load the testing environment file
    try:

        # Open the secret settings JSON file and load it's content
        with open(os.path.join(BASE_DIR, 'testing-secrets.json')) as fi_handle:
            SECRETS = json.load(fi_handle)
        warnings.warn("Secrets values loaded from the testing environment file")

    except IOError:

        # Fallback for debug environment (no secrets file or testing file)
        SECRETS = {}
        warnings.warn("No secrets file available, fallback to default values")

# Load custom override for default values
this_module = globals()
for key, value in SECRETS.items():
    this_module[key] = value


# endregion

# region ----- Core settings

# Secret key for cryptographic signing
# SECURITY WARNING: keep the secret key used in production secret!
# See https://docs.djangoproject.com/en/1.9/ref/settings/#secret-key
SECRET_KEY = SECRETS.get('SECRET_KEY', 'the totally not secret key for debug')

# A string representing the full Python import path to your root URLconf.
# See https://docs.djangoproject.com/en/1.9/ref/settings/#root-urlconf
ROOT_URLCONF = 'skcodeonlinetester.urls'

# The full Python path of the WSGI application object that Django’s built-in servers will use.
# See https://docs.djangoproject.com/en/1.9/ref/settings/#wsgi-application
WSGI_APPLICATION = 'skcodeonlinetester.wsgi.dev.application'

# List of directories searched for fixture files, in addition to the fixtures
# directory of each application, in search order.
# See https://docs.djangoproject.com/en/1.9/ref/settings/#std:setting-FIXTURE_DIRS
FIXTURE_DIRS = [
    os.path.join(BASE_DIR, 'fixtures'),
]

# When set to True, if the request URL does not match any of the patterns in the URLconf
# and it doesn’t end in a slash, an HTTP redirect is issued to the same URL with a slash appended.
# See https://docs.djangoproject.com/en/1.9/ref/settings/#append-slash
APPEND_SLASH = True

# Whether to prepend the “www.” subdomain to URLs that don’t have it.
# See https://docs.djangoproject.com/en/1.9/ref/settings/#prepend-www
PREPEND_WWW = False

# endregion

# region ----- Internationalization and localization settings
# See https://docs.djangoproject.com/en/1.9/topics/i18n/

# Default language code of the project
# See https://docs.djangoproject.com/en/1.9/ref/settings/#language-code
LANGUAGE_CODE = 'fr'

# The name of the cookie to use for the language cookie.
# See https://docs.djangoproject.com/en/1.9/ref/settings/#language-cookie-name
LANGUAGE_COOKIE_NAME = 'user_language'

# A tuple of all available languages.
# See https://docs.djangoproject.com/en/1.9/ref/settings/#languages
LANGUAGES = [
    ('fr', _('French')),
    ('en', _('English')),
]

# Set to true to enable string language translation
# See https://docs.djangoproject.com/en/1.9/ref/settings/#use-i18n
USE_I18N = True

# Set to true to enable localized format (like date and numbers)
# See https://docs.djangoproject.com/en/1.9/ref/settings/#use-l10n
USE_L10N = True

# Default time zone of the server
# See https://docs.djangoproject.com/en/1.9/ref/settings/#time-zone
TIME_ZONE = 'Europe/Paris'

# Set to true to enable localized time zone (like GMT+1)
# See https://docs.djangoproject.com/en/1.9/ref/settings/#use-tz
USE_TZ = True

# Default first day of week, to be used on calendars
# 0 means Sunday, 1 means Monday...
# See https://docs.djangoproject.com/en/1.9/ref/settings/#first-day-of-week
FIRST_DAY_OF_WEEK = 1

# endregion

# region ----- Email and error notification settings

# List of admin mails, will get mailed when DEBUG=False and something goes terribly wrong
# See https://docs.djangoproject.com/en/1.9/ref/settings/#admins
ADMINS = SECRETS.get('ADMINS', [])

# List of managers mails, will get mailed when a broken link is requested
# Require BrokenLinkEmailsMiddleware to be enabled to work
# See https://docs.djangoproject.com/en/1.9/ref/settings/#managers
MANAGERS = SECRETS.get('MANAGERS', [])

# List of (compiled) regex describing URLs that should be ignored when reporting HTTP 404 errors via email
# See https://docs.djangoproject.com/en/1.9/ref/settings/#ignorable-404-urls
IGNORABLE_404_URLS = []

# endregion

# region ----- Cache settings

# Key prefix for all cache key
# Declared here once, then use in concrete settings
# https://docs.djangoproject.com/fr/1.9/ref/settings/#key-prefix
CACHE_KEY_PREFIX = 'skcd1'

# The cache backend alias to use for the per-site cache
# See https://docs.djangoproject.com/en/1.9/ref/settings/#std:setting-CACHE_MIDDLEWARE_ALIAS
CACHE_MIDDLEWARE_ALIAS = 'default'

# Key prefix for the cache middleware
# See https://docs.djangoproject.com/en/1.9/ref/settings/#std:setting-CACHE_MIDDLEWARE_KEY_PREFIX
CACHE_MIDDLEWARE_KEY_PREFIX = 'cachemdw'

# Lifetime duration of the cache from the cache middleware in seconds
# See https://docs.djangoproject.com/en/1.9/ref/settings/#std:setting-CACHE_MIDDLEWARE_SECONDS
CACHE_MIDDLEWARE_SECONDS = 60 * 60 * 24  # 24 hours

# endregion

# region ----- Email settings

# Subject prefix of emails sent to ADMINS and MANAGERS
# See https://docs.djangoproject.com/en/1.9/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = '[PySkCode Online Tester] '

# The email address that error messages come from (used with ADMINS and MANAGERS)
# See https://docs.djangoproject.com/en/1.9/ref/settings/#std:setting-SERVER_EMAIL
# FIXME Currently reuse CDM mail relay service
SERVER_EMAIL = 'notifications@carnetdumaker.net'

# 'From' address for all mail sent with send_mail()
# See https://docs.djangoproject.com/en/1.9/ref/settings/#std:setting-DEFAULT_FROM_EMAIL
# FIXME Currently reuse CDM mail relay service
DEFAULT_FROM_EMAIL = 'notifications@carnetdumaker.net'

# SMTP settings
EMAIL_HOST = SECRETS.get('EMAIL_HOST', 'localhost')
EMAIL_PORT = SECRETS.get('EMAIL_PORT', 25)
EMAIL_HOST_USER = SECRETS.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = SECRETS.get('EMAIL_HOST_PASSWORD', '')
EMAIL_USE_TLS = SECRETS.get('EMAIL_USE_TLS', False)

# endregion

# region ----- User agents filtering settings

# List of (compiled) regex representing User-Agent strings that are not allowed to visit any page
# See https://docs.djangoproject.com/en/1.9/ref/settings/#disallowed-user-agents
DISALLOWED_USER_AGENTS = []

# endregion

# region ----- Application definition

# List of all applications that are enabled in this Django installation
# See https://docs.djangoproject.com/en/1.9/ref/settings/#installed-apps
INSTALLED_APPS = [

    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',

    # Local apps
    'apps.home',
    'apps.bootstrapform',
]

# List of all middleware that are enabled in this Django installation
# See https://docs.djangoproject.com/en/1.9/ref/settings/#middleware-classes
MIDDLEWARE_CLASSES = [
    # 'django.middleware.security.SecurityMiddleware ',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# endregion

# region ----- Database settings

# Database settings
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': SECRETS.get('DATABASE_NAME', 'vagrant'),
        'USER': SECRETS.get('DATABASE_USER', 'vagrant'),
        'PASSWORD': SECRETS.get('DATABASE_PASSWORD', 'vagrant'),
        'HOST': SECRETS.get('DATABASE_HOST', '')  # If blank: use UNIX domain socket (local lines in pg_hba.conf)
    }
}

# endregion

# region ----- Media and files upload settings

# Maximum size in bytes of a request before it will be streamed to the file system instead of memory.
# See https://docs.djangoproject.com/en/1.9/ref/settings/#file-upload-max-memory-size
FILE_UPLOAD_MAX_MEMORY_SIZE = 1024 * 1024 * 2.5  # 2.5Mo

# The numeric mode to set newly uploaded files to.
# DO NOT FORGET THE 0o (octal) prefix!
# See https://docs.djangoproject.com/en/1.9/ref/settings/#std:setting-FILE_UPLOAD_PERMISSIONS
FILE_UPLOAD_PERMISSIONS = 0o644

# The numeric mode to apply to directories created in the process of uploading files.
# DO NOT FORGET THE 0 (octal) prefix!
# See https://docs.djangoproject.com/en/1.9/ref/settings/#std:setting-FILE_UPLOAD_DIRECTORY_PERMISSIONS
FILE_UPLOAD_DIRECTORY_PERMISSIONS = 0o755

# Absolute filesystem path to the directory that will hold user-uploaded files
# See https://docs.djangoproject.com/en/1.9/ref/settings/#media-root
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')

# URL that handles the media served from MEDIA_ROOT.
# It must end in a slash if set to a non-empty value.
# See https://docs.djangoproject.com/en/1.9/ref/settings/#media-url
MEDIA_URL = '/uploads/'

# endregion

# region ----- Static files upload settings
# See https://docs.djangoproject.com/en/1.9/howto/static-files/

# The absolute path to the directory where collectstatic will collect static files for deployment.
# See https://docs.djangoproject.com/en/1.9/ref/settings/#static-root
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# URL to use when referring to static files located in STATIC_ROOT.
# See https://docs.djangoproject.com/en/1.9/ref/settings/#static-url
STATIC_URL = '/static/'

# This setting defines the additional locations the staticfiles app
# will traverse if the FileSystemFinder finder is enabled.
# See https://docs.djangoproject.com/en/1.9/ref/settings/#staticfiles-dirs
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# The file storage engine to use when collecting static files with the collectstatic management command.
# See https://docs.djangoproject.com/en/1.9/ref/settings/#std:setting-STATICFILES_STORAGE
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

# The list of finder backends that know how to find static files in various locations.
# See https://docs.djangoproject.com/en/1.9/ref/settings/#staticfiles-finders
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# endregion

# region ----- Template settings

# Template settings
# See https://docs.djangoproject.com/en/1.8/ref/templates/upgrading/
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': False,
            'context_processors': [
                # Standard context processors
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                # 'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',

                # Custom context processors
                'skcodeonlinetester.context_processors.app_constants',
            ],
            'string_if_invalid': '!-%s-!',
        },
    },
]

# endregion

# region ----- XFrame settings
# See https://docs.djangoproject.com/en/1.9/ref/clickjacking/

# Click jacking options
# See https://docs.djangoproject.com/en/1.9/ref/settings/#std:setting-X_FRAME_OPTIONS
X_FRAME_OPTIONS = 'SAMEORIGIN'

# User-side XSS protection
# See https://docs.djangoproject.com/en/1.9/ref/settings/#secure-browser-xss-filter
SECURE_BROWSER_XSS_FILTER = True

# endregion

# region ----- Sessions settings

# Age of cookie, in seconds
# See https://docs.djangoproject.com/en/1.9/ref/settings/#session-cookie-age
SESSION_COOKIE_AGE = 60 * 60 * 24 * 7 * 4  # 4 weeks

# Set to true to disallow access of session cookies by javascript
# See https://docs.djangoproject.com/en/1.9/ref/settings/#session-cookie-httponly
SESSION_COOKIE_HTTPONLY = True

# backend used to store session data
# See https://docs.djangoproject.com/en/1.9/ref/settings/#session-engine
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

# endregion

# region ----- CSRF settings

# Set to true to disallow CSRF cookies access from javascript
# See https://docs.djangoproject.com/en/1.9/ref/settings/#csrf-cookie-httponly
CSRF_COOKIE_HTTPONLY = False
# Don't set to true, otherwise Ajax forms will be fucked up

# endregion

# region ----- Django-site settings

# Current Django site identifier
# See https://docs.djangoproject.com/en/1.9/ref/settings/#site-id
SITE_ID = SECRETS.get('SITE_ID', 1)

# endregion
