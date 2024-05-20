import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = 'django-insecure-8=bdfgnhjhgfsdndfhdgfhnfhmgfkr#*=alt#+glyh7uef-2v@#-'

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'deadyoux.pythonanywhere.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/home/DeadYouX/SeregaPirate/db.sqlite3',
    }
}

STATIC_URL = 'static/'
STATIC_ROOT = '/home/DeadYouX/SeregaPirate/static/'


STATICFILES_DIRS = [
    BASE_DIR + "main/static",
]