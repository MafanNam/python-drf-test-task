import os

from django.core.wsgi import get_wsgi_application
from environ import Env

env = Env()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", env("DJANGO_SETTINGS_MODULE", default="backend.settings.local"))

application = get_wsgi_application()
