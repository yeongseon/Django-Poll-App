#!/usr/bin/env python
import os
import sys
from dotenv import load_dotenv

if __name__ == '__main__':
    """Run administrative tasks."""
    # If WEBSITE_HOSTNAME is defined as an environment variable, then we're running on Azure App Service

    # Only for Local Development - Load environment variables from the .env file
    if not 'WEBSITE_HOSTNAME' in os.environ:
        print("Loading environment variables for .env file")
        load_dotenv('./.env')

    # When running on Azure App Service you should use the production settings.
    settings_module = "pollme.production" if 'WEBSITE_HOSTNAME' in os.environ else 'pollme.settings'    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)