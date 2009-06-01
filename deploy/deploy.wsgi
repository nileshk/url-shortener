import os
import sys

# redirect sys.stdout to sys.stderr for bad libraries like geopy that uses
# print statements for optional import exceptions.
sys.stdout = sys.stderr

from os.path import abspath, dirname, join
from site import addsitedir

PROJECT_ROOT = abspath(join(dirname(__file__), "../"))

sys.path.insert(0, PROJECT_ROOT)
sys.path.insert(0, abspath(join(dirname(__file__), "../../")))

from django.core.handlers.wsgi import WSGIHandler

os.environ["DJANGO_SETTINGS_MODULE"] = "urlweb.settings"

application = WSGIHandler()
