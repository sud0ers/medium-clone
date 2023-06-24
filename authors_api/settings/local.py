from . base import * #noqa
from .base import env

SECRET_KEY = env("DJANGO_SECRET_KEY",
                 default = "JLQQMYdgIdv0KUBTfKXJHf8UlErbRyf5K3Rhngw_mxy-MH7I3Vg",
                 )

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]