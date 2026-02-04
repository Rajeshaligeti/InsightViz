"""
Vercel serverless entry point.
Exposes the WSGI callable as `app` (required by Vercel Python runtime).
"""
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'InsightViz.settings')

from django.core.wsgi import get_wsgi_application

# On Vercel, DB is in /tmp; ensure migrations are applied (idempotent)
if os.environ.get('VERCEL'):
    import django
    django.setup()
    from django.core.management import call_command
    call_command('migrate', '--noinput', verbosity=0)

app = get_wsgi_application()
