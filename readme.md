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

4. Modificamos el archivo settings.py

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

