#!/usr/bin/python
import sys, os

# Add a custom Python path.
sys.path.insert(0, "/home/riverbird/python/django/demo")

# Set the DJANGO_SETTINGS_MODULE environment variable.
os.environ['DJANGO_SETTINGS_MODULE'] = "settings"

from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")
