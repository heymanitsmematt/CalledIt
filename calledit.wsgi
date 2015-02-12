import os
import sys
sys.path.append('/calledit/CalledIt/calledit')
os.environ['DJANGO_SETTINGS_MODULE'] = 'calledit.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
