#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from django.core.asgi import get_asgi_application  # Import the ASGI app

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'JaWa.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

# If the file is used in a serverless context, define `app`
# This allows Vercel to run the ASGI app
if 'VERCEL' in os.environ:  # This check helps to identify if running on Vercel
    app = get_asgi_application()  # Set up the ASGI app for serverless functions

if __name__ == '__main__':
    main()
