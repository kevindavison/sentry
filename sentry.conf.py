import os

import dj_database_url


SECRET_KEY = '*a&r#ql7pii7awl*xre(&j1@q-z4j2)@l)o5hu7=^emno!hx1%'

DATABASES = {
    'default': dj_database_url.config()
}

SENTRY_KEY = os.environ.get(
    'SENTRY_KEY', '80)30e+no5ulv9*bv8jnkrz90nf2qjfg*u3rypw@n8^_9tpvu#')

print os.environ

print os.environ['ENVIRONMENT']

# Set this to false to require authentication
SENTRY_PUBLIC = False
SENTRY_ALLOW_REGISTRATION = False

SERVER_EMAIL = os.environ.get('SENTRY_EMAIL_FROM', 'root@localhost')

# The absolute URI to Sentry
SENTRY_URL_PREFIX = os.environ['SENTRY_URL_PREFIX']

SENTRY_WEB_HOST = '0.0.0.0'
SENTRY_WEB_PORT = 3000
SENTRY_WEB_OPTIONS = {
    # the number of gunicorn workers
    'workers': 3,
    # detect HTTPS mode from X-Forwarded-Proto header
    'secure_scheme_headers': {'X-FORWARDED-PROTO': 'https'},
}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = os.environ['SENDGRID_USERNAME']
EMAIL_HOST_PASSWORD = os.environ['SENDGRID_PASSWORD']
EMAIL_PORT = 587
EMAIL_USE_TLS = True

GITHUB_APP_ID = '9f045cdbc059bfdf5869'
GITHUB_API_SECRET = 'a540ff1fc93b5131f10ef6411972d0014c1110f3'
GITHUB_EXTENDED_PERMISSIONS = ['vidahealth/webserver']
