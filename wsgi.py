import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'banjo.settings_heroku')
application = get_wsgi_application()
from app import views