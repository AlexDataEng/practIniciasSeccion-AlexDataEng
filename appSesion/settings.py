# settings.py en la aplicación

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_URL = '/appSesion/static/'  # URL para archivos estáticos de la aplicación
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'appSesion/static')]  # Ruta al directorio static de la aplicación

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'appSesion/template')],  # Ruta al directorio templates de la aplicación
        'APP_DIRS': True,
        # ...
    },
]
