import os
from configparser import RawConfigParser

from .base import *

# TODO: fix ALLOWED_HOSTS
# jakým mechanismem běží mojeknihovna.eu - není v sites-enabled

config = RawConfigParser()
config['DEFAULT'] = {'ALLOWED_HOSTS': '*'}   # toto asi nechodí
config.read('/etc/django/wagtail1/env.ini')


DEBUG = False
SECRET_KEY = os.environ.get('MZ_SECRET_KEY') or config.get('main', 'SECRET_KEY')
# v ALLOWED_HOSTS musí být i www.<domena>, tj. např. <domena>,www.<domena>,*.<domena>
ALLOWED_HOSTS = (os.environ.get('MZ_ALLOWED_HOSTS') or config.get('main', 'ALLOWED_HOSTS')
                 ).replace(',', ' ').replace(';', ' ').split()

X_FRAME_OPTIONS = 'DENY'
SECURE_HSTS_SECONDS = 300
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True


try:
    from .local import *
except ImportError:
    pass
