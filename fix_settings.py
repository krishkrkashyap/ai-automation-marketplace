import re

with open('C:/Users/krish/ai-automation-marketplace/core/settings.py', 'r') as f:
    content = f.read()

old = '''from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-6vgo(qs=&e)y8ag+*g1!3y)eewdpwmolisp-xnq3z9)ee&34z#'

DEBUG = True

ALLOWED_HOSTS = ['*']'''

new = '''import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-6vgo(qs=&e)y8ag+*g1!3y)eewdpwmolisp-xnq3z9)ee&34z#')

DEBUG = os.environ.get('DEBUG', 'True') == 'True'

ALLOWED_HOSTS = ['*']

if os.environ.get('DATABASE_URL'):
    import dj_database_url
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }'''

content = content.replace(old, new)

with open('C:/Users/krish/ai-automation-marketplace/core/settings.py', 'w') as f:
    f.write(content)

print('Settings updated')