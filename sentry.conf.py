import os.path
import os

import dj_database_url


SECRET_KEY = '*a&r#ql7pii7awl*xre(&j1@q-z4j2)@l)o5hu7=^emno!hx1%'

DATABASES = {
    'default': dj_database_url.config()
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
SENTRY_WEB_PORT = 3000
SENTRY_WEB_OPTIONS = {
    'workers': 3,  # the number of gunicorn workers
    'secure_scheme_headers': {'X-FORWARDED-PROTO': 'https'},  # detect HTTPS mode from X-Forwarded-Proto header
}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = os.environ['SENDGRID_USERNAME']
EMAIL_HOST_PASSWORD = os.environ['SENDGRID_PASSWORD']
EMAIL_PORT = 587
EMAIL_USE_TLS = True

ALLOWED_HOSTS=['*']
