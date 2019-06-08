"""
WSGI config for GuidedLearningSolution project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os, sys
sys.path.append('C:/Users/Programator/Bitnami Django Stack projects/GuidedLearningSolution')
os.environ.setdefault("PYTHON_EGG_CACHE", "C:/Users/Programator/Bitnami Django Stack projects/GuidedLearningSolution/egg_cache")


from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GuidedLearningSolution.settings')

application = get_wsgi_application()
