import os

from django.core.asgi import get_asgi_application
from environ import Env

env = Env()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", env("DJANGO_SETTINGS_MODULE", default="backend.settings.local"))

application = get_asgi_application()
