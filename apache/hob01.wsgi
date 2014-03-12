import os
import sys

import site

VE = '/home/bgriffin/.virtualenvs/django'
site.addsitedir(VE + '/lib/python2.7/site-packages')

os.environ['DJANGO_SETTINGS_MODULE'] = 'hob01.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

path = '/home/bgriffin/www/hob01'
if path not in sys.path:
    sys.path.append(path)
