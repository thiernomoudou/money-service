import os
from myproject.settings import *

ALLOWED_HOSTS = [ 'test.tsdiallo.com', '207.154.254.143']
DEBUG = False
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['NAME'],
        'USER': os.environ['USER'],
        'PASSWORD': os.environ['PASSWORD'],
        'HOST': 'localhost',
        'PORT': '',
    }
}

