from settings_base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'sqlite_database/{{ project_name }}.dev',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'dmalik5',
        'PASSWORD': 'unix123',
        'HOST': '192.168.1.102',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '5432',                      # Set to empty string for default.
    }
}
