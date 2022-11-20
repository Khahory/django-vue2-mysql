PASOS PARA INIT EL PROYECTO

1. Creamos la carpeta de backend

``
mkdir backend
``

2. Instalamos los requerimientos

django==4.1.3
django-cors-headers==3.13.0
djangorestframework==3.14.0
django-environ==0.9.0
pillow==9.3.0

3. Creamos el proyecto django

``
django-admin startproject core .
``

4. Modificamos el archivo settings.py agregando nuestras variables env

````python

# TRABAJAR CON LAS API
from corsheaders.defaults import default_headers
import os
import environ

env = environ.Env(
    # predeterminado vene False DEBUG
    DENUG=(bool, False)
)
# reading .env file
environ.Env.read_env()

SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG')
````

5. Agregamos nustras APPS a django

```
    'core',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
```

6. Agregamos el middleware de corsheaders

```
    # Corsheaders
    "corsheaders.middleware.CorsMiddleware",
```

7. Agregamos que dominios pueden ver nuestra APP

```
# aqui le decimos a quien permitimos que vea nuestra API
CORS_ORIGIN_WHITELIST = (
    'http://localhost:8000',
    'http://127.0.0.1:8000',

    'http://localhost:8080',
    'http://127.0.0.1:8080',

    'http://localhost:3000',
    'http://127.0.0.1:3000',
)

CORS_ALLOW_HEADERS = list(default_headers) + [
    'contenttype',
]
```

8. Agregamos y creamos (en backend) las carpetas estaticas

```python
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

9. En urls.py debemos agregar estas configuraciones

```
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    ...
    
    path('api-auth/', include('rest_framework.urls'))
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

10. En settings.py agregamos el siguiente codigo a lo ultimo

```
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ]
}
```

11. Creamos el modelo y la importamos en settings.py

```
python manage.py startapp anime
```

12. Despues de crear un modelos debemos hacer migraciones

```
python manage.py makemigrations
python manage.py migrate
```