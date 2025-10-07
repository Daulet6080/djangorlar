#!/usr/bin/env python
import os
import sys
from settings.conf import ENV_ID, ENV_POSSIBLE_OPTIONS   # 👈 добавь этот импорт

def main():
    """Run administrative tasks."""
    assert ENV_ID in ENV_POSSIBLE_OPTIONS, (
        f"Set correct DJANGORLAR_ENV_ID env var. Possible options: {ENV_POSSIBLE_OPTIONS}"
    )
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'settings.env.{ENV_ID}')

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
