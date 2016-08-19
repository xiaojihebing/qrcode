# -*- coding: utf-8 -*-
import sys
import os

root = os.path.dirname(__file__)
#sys.path.insert(0, os.path.join(root, 'site-packages.zip'))

from mysite import wsgi
import sae
application = sae.create_wsgi_app(wsgi.application)