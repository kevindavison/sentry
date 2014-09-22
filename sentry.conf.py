import os.path
import os


SECRET_KEY = '*a&r#ql7pii7awl*xre(&j1@q-z4j2)@l)o5hu7=^emno!hx1%'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

SENTRY_KEY = os.environ.get(
    'SENTRY_KEY', '80)30e+no5ulv9*bv8jnkrz90nf2qjfg*u3rypw@n8^_9tpvu#')


# Set this to false to require authentication
SENTRY_PUBLIC = False
SENTRY_ALLOW_REGISTRATION = False

SERVER_EMAIL = os.environ.get('SENTRY_EMAIL_FROM', 'root@localhost')

# You should configure the absolute URI to Sentry. It will attempt to guess it if you don't
# but proxies may interfere with this.
SENTRY_URL_PREFIX = os.environ.get('SENTRY_URL_PREFIX', '')

SENTRY_WEB_HOST = '0.0.0.0'
SENTRY_WEB_PORT = 9000
SENTRY_WEB_OPTIONS = {
    'workers': 3,  # the number of gunicorn workers
    'secure_scheme_headers': {'X-FORWARDED-PROTO': 'https'},  # detect HTTPS mode from X-Forwarded-Proto header
}

# Mail server configuration

# For more information check Django's documentation:
#  https://docs.djangoproject.com/en/1.3/topics/email/?from=olddocs#e-mail-backends

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' if os.environ.get('SENTRY_EMAIL_ENABLED') else 'django.core.mail.backends.console.EmailBackend'

EMAIL_HOST = os.environ.get('SENTRY_EMAIL_HOST', 'localhost')
EMAIL_HOST_PASSWORD = os.environ.get('SENTRY_EMAIL_PASSWORD', '')
EMAIL_HOST_USER = os.environ.get('SENTRY_EMAIL_USER','')
EMAIL_PORT = os.environ.get('SENTRY_EMAIL_PORT', 25)
EMAIL_USE_TLS = os.environ.get('SENTRY_EMAIL_USE_TLS', False)

# http://twitter.com/apps/new
# It's important that input a callback URL, even if its useless. We have no idea why, consult Twitter.
TWITTER_CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY')
TWITTER_CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET')

# http://developers.facebook.com/setup/
FACEBOOK_APP_ID = os.environ.get('FACEBOOK_APP_ID')
FACEBOOK_API_SECRET = os.environ.get('FACEBOOK_APP_SECRET')

# http://code.google.com/apis/accounts/docs/OAuth2.html#Registering
GOOGLE_OAUTH2_CLIENT_ID = os.environ.get('GOOGLE_OAUTH2_CLIENT_ID')
GOOGLE_OAUTH2_CLIENT_SECRET = os.environ.get('GOOGLE_OAUTH2_CLIENT_SECRET')

# https://github.com/settings/applications/new
GITHUB_APP_ID = os.environ.get('GITHUB_APP_ID')
GITHUB_API_SECRET = os.environ.get('GITHUB_APP_SECRET')

# https://trello.com/1/appKey/generate
TRELLO_API_KEY = os.environ.get('TRELLO_API_KEY')
TRELLO_API_SECRET = os.environ.get('TRELLO_API_SECRET')

ALLOWED_HOSTS=['*']
