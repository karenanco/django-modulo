# 🧑‍💻 Django 6.0 - Superusuario, Archivos del Proyecto y Primera Aplicación

Este documento continúa la configuración inicial de un proyecto Django 6.0.

Aquí aprenderás:

1. Cómo crear un superusuario.
2. Para qué sirve cada archivo principal del proyecto.
3. Cómo crear la primera aplicación dentro del proyecto.

---

# 1. Crear un Superusuario en Django

## ¿Qué es un superusuario?

Un **superusuario** es un usuario especial con permisos completos dentro del proyecto Django.

Este usuario puede acceder al panel de administración de Django y realizar acciones como:

- Crear usuarios.
- Editar usuarios.
- Eliminar usuarios.
- Administrar modelos registrados.
- Ver información interna del sistema.
- Gestionar contenido desde una interfaz visual.

---

## ¿Para qué sirve el panel de administración?

Django incluye un panel administrativo listo para usar.

Este panel permite administrar datos del sistema sin tener que crear una interfaz desde cero.

Por ejemplo, desde el administrador podríamos gestionar:

- Productos.
- Clientes.
- Categorías.
- Pedidos.
- Usuarios.
- Roles.
- Publicaciones.
- Comentarios.

La ruta por defecto del panel de administración es:

```txt
http://127.0.0.1:8000/admin/
```

---

## Paso 1: Ejecutar migraciones

Antes de crear el superusuario, asegúrate de haber ejecutado las migraciones iniciales:

```bash
python manage.py migrate
```

Este comando crea las tablas internas que Django necesita para trabajar con usuarios, permisos y sesiones.

---

## Paso 2: Crear el superusuario

Ejecuta el siguiente comando:

```bash
python manage.py createsuperuser
```

Django solicitará algunos datos:

```txt
Username:
Email address:
Password:
Password again:
```

Ejemplo:

```txt
Username: admin
Email address: admin@correo.com
Password: ********
Password again: ********
```

---

## Importante sobre la contraseña

Cuando escribas la contraseña, la terminal no mostrará los caracteres.

Esto es normal por seguridad.

Aunque no veas nada en pantalla, la contraseña sí se está escribiendo.

---

## Paso 3: Ejecutar el servidor

Una vez creado el superusuario, inicia el servidor:

```bash
python manage.py runserver
```

Luego entra en el navegador a:

```txt
http://127.0.0.1:8000/admin/
```

---

## Paso 4: Iniciar sesión

Ingresa con el usuario y contraseña creados.

Si todo está correcto, verás el panel administrativo de Django.

---

# 2. Explicación Detallada de los Archivos del Proyecto

Cuando creamos el proyecto con:

```bash
django-admin startproject core .
```

Django genera una estructura parecida a esta:

```txt
proyecto/
│
├── manage.py
│
├── requirements.txt
│
├── venv/
│
└── core/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

---

## manage.py

`manage.py` es el archivo principal para ejecutar comandos de Django desde la terminal.

Con este archivo podemos:

- Levantar el servidor.
- Crear aplicaciones.
- Ejecutar migraciones.
- Crear superusuarios.
- Entrar al shell de Django.
- Ejecutar pruebas.

Ejemplos:

```bash
python manage.py runserver
python manage.py migrate
python manage.py createsuperuser
python manage.py startapp productos
```

---

## requirements.txt

`requirements.txt` contiene la lista de librerías necesarias para que el proyecto funcione.

Ejemplo:

```txt
Django==6.0
python-decouple==3.8
psycopg2-binary==2.9.9
django-extensions==3.2.3
gunicorn==21.2.0
```

Sirve para instalar todas las dependencias usando:

```bash
pip install -r requirements.txt
```

---

## Carpeta core/

La carpeta `core/` representa la configuración principal del proyecto.

Normalmente contiene los archivos globales de Django.

No es una aplicación como tal, sino el centro de configuración del proyecto.

---

## core/__init__.py

Este archivo puede estar vacío.

Su función es indicar que la carpeta `core` debe ser tratada como un paquete de Python.

Un paquete en Python es una carpeta que puede contener módulos importables.

---

## core/settings.py

Es uno de los archivos más importantes del proyecto.

Aquí se encuentra la configuración general de Django.

Contiene información como:

- Aplicaciones instaladas.
- Base de datos.
- Idioma.
- Zona horaria.
- Archivos estáticos.
- Middleware.
- Seguridad.
- Configuración de templates.
- Clave secreta del proyecto.

### INSTALLED_APPS

Dentro de `settings.py` encontrarás una sección como esta:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

Aquí se registran las aplicaciones que Django usará.

Cuando creemos nuestra primera app, también deberemos agregarla en esta lista.

### DATABASES

También encontrarás la configuración de base de datos:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

Por defecto, Django usa SQLite.

SQLite es útil para aprender y desarrollar proyectos pequeños.

En producción, normalmente se recomienda PostgreSQL.

### LANGUAGE_CODE

Define el idioma del proyecto.

```python
LANGUAGE_CODE = 'es-cl'
```

### TIME_ZONE

Define la zona horaria del proyecto.

```python
TIME_ZONE = 'America/Santiago'
```

### STATIC_URL

Define la ruta base para archivos estáticos.

Los archivos estáticos pueden ser:

- CSS
- JavaScript
- Imágenes
- Fuentes

```python
STATIC_URL = 'static/'
```

---

## core/urls.py

Este archivo funciona como el enrutador principal del proyecto.

Aquí se definen las rutas generales.

Ejemplo inicial:

```python
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
```

Esta línea permite acceder al panel administrativo:

```python
path('admin/', admin.site.urls)
```

Por eso el admin funciona en:

```txt
http://127.0.0.1:8000/admin/
```

---

## core/asgi.py

Archivo usado para ejecutar el proyecto con servidores ASGI.

ASGI permite trabajar con funcionalidades modernas como:

- WebSockets.
- Comunicación en tiempo real.
- Aplicaciones asíncronas.

En clases iniciales normalmente no se modifica.

---

## core/wsgi.py

Archivo usado para ejecutar el proyecto en servidores WSGI.

WSGI es el estándar tradicional para desplegar aplicaciones Python web.

Por ejemplo, se puede usar junto con:

- Gunicorn.
- Nginx.
- Apache.

En clases iniciales normalmente no se modifica.

---

# 3. Crear la Primera Aplicación en Django

## ¿Qué es una aplicación en Django?

En Django, un proyecto puede tener varias aplicaciones.

El proyecto es la estructura general.

Las aplicaciones son módulos internos que representan funcionalidades específicas.

Por ejemplo, en un ecommerce podríamos tener:

```txt
proyecto ecommerce
│
├── app productos
├── app clientes
├── app pedidos
├── app pagos
└── app usuarios
```

Cada app se encarga de una parte del sistema.

---

## Diferencia entre proyecto y aplicación

| Concepto | Explicación |
|---|---|
| Proyecto | Configuración general del sistema completo. |
| Aplicación | Módulo específico con una funcionalidad concreta. |

Ejemplo:

```txt
Proyecto: tienda_online
Aplicaciones: productos, clientes, ventas, pagos
```

---

## Paso 1: Crear la aplicación

Para crear una app llamada `productos`, ejecuta:

```bash
python manage.py startapp productos
```

Esto generará una carpeta llamada:

```txt
productos/
```

---

## Paso 2: Estructura de la aplicación

Después de crear la app, verás una estructura como esta:

```txt
productos/
│
├── __init__.py
├── admin.py
├── apps.py
├── models.py
├── tests.py
├── views.py
└── migrations/
    └── __init__.py
```

---

# 4. Explicación de los Archivos de la Aplicación

## productos/__init__.py

Indica que la carpeta `productos` es un paquete de Python.

Normalmente queda vacío.

---

## productos/admin.py

Se usa para registrar modelos en el panel administrativo de Django.

Por ejemplo, si creamos un modelo `Producto`, debemos registrarlo aquí para verlo en el admin.

```python
from django.contrib import admin
from .models import Producto

admin.site.register(Producto)
```

---

## productos/apps.py

Contiene la configuración de la aplicación.

```python
from django.apps import AppConfig

class ProductosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'productos'
```

El valor importante es:

```python
name = 'productos'
```

Ese nombre representa la app dentro del proyecto.

---

## productos/models.py

Aquí se crean los modelos de la aplicación.

Un modelo representa una tabla de la base de datos.

```python
from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre
```

Este modelo representa una tabla de productos.

---

## productos/views.py

Aquí se crean las vistas.

Una vista es una función o clase que recibe una petición del navegador y devuelve una respuesta.

```python
from django.http import HttpResponse

def inicio(request):
    return HttpResponse("Hola desde la app productos")
```

---

## productos/tests.py

Se usa para escribir pruebas automáticas.

Las pruebas permiten verificar que el código funciona correctamente.

```python
from django.test import TestCase

class ProductoTest(TestCase):
    def test_ejemplo(self):
        self.assertEqual(1 + 1, 2)
```

En una primera clase, normalmente no se modifica todavía.

---

## productos/migrations/

Esta carpeta almacena los cambios que se hacen en los modelos.

Cuando creamos o modificamos modelos, Django genera archivos de migración.

Estos archivos sirven para transformar los modelos en tablas reales dentro de la base de datos.

---

# 5. Registrar la Aplicación en settings.py

Crear la app no es suficiente.

También debemos registrarla en el archivo:

```txt
core/settings.py
```

Busca la lista:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

Agrega la aplicación al final:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'productos',
]
```

También se puede registrar usando la clase de configuración:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'productos.apps.ProductosConfig',
]
```

Ambas formas funcionan, pero la segunda es más explícita.

---

# 6. Crear una Primera Vista

En el archivo:

```txt
productos/views.py
```

Escribe:

```python
from django.http import HttpResponse

def inicio(request):
    return HttpResponse("Hola, esta es mi primera aplicación en Django")
```

---

# 7. Crear un Archivo urls.py en la App

Por defecto, la app no trae su propio archivo de rutas.

Debemos crearlo manualmente.

Dentro de la carpeta `productos/`, crea un archivo llamado:

```txt
urls.py
```

La estructura quedaría así:

```txt
productos/
│
├── admin.py
├── apps.py
├── models.py
├── tests.py
├── views.py
├── urls.py
└── migrations/
```

Dentro de `productos/urls.py`, escribe:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio_productos'),
]
```

---

# 8. Conectar las Rutas de la App con el Proyecto

Ahora debemos conectar las rutas de `productos` con las rutas principales del proyecto.

Abre:

```txt
core/urls.py
```

Código original:

```python
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
```

Modifícalo así:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('productos/', include('productos.urls')),
]
```

---

## ¿Qué hace include?

```python
include('productos.urls')
```

Le dice a Django:

> Cuando alguien entre a una ruta que comience con `productos/`, busca las rutas dentro del archivo `productos/urls.py`.

Entonces esta ruta:

```txt
http://127.0.0.1:8000/productos/
```

Ejecutará la vista:

```python
views.inicio
```

---

# 9. Probar la Aplicación

Ejecuta el servidor:

```bash
python manage.py runserver
```

Abre el navegador y visita:

```txt
http://127.0.0.1:8000/productos/
```

Deberías ver:

```txt
Hola, esta es mi primera aplicación en Django
```

---

# 10. Crear el Primer Modelo Producto

En:

```txt
productos/models.py
```

Agrega:

```python
from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio = models.IntegerField()
    stock = models.IntegerField()
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
```

---

## Explicación del modelo

| Campo | Tipo | Explicación |
|---|---|---|
| `nombre` | `CharField` | Texto corto. |
| `descripcion` | `TextField` | Texto largo. |
| `blank=True` | Validación | Permite que el campo esté vacío en formularios. |
| `precio` | `IntegerField` | Número entero. |
| `stock` | `IntegerField` | Número entero. |
| `creado_en` | `DateTimeField` | Fecha y hora de creación automática. |
| `auto_now_add=True` | Configuración | Guarda la fecha solo al crear el registro. |

---

# 11. Crear Migraciones del Modelo

Cuando creas o modificas un modelo, debes generar una migración:

```bash
python manage.py makemigrations
```

Este comando crea un archivo dentro de:

```txt
productos/migrations/
```

Luego aplica la migración:

```bash
python manage.py migrate
```

Esto crea la tabla en la base de datos.

---

# 12. Registrar el Modelo en el Admin

Para poder ver el modelo `Producto` en el panel administrativo, abre:

```txt
productos/admin.py
```

Y escribe:

```python
from django.contrib import admin
from .models import Producto

admin.site.register(Producto)
```

---

# 13. Probar en el Panel Admin

Ejecuta el servidor:

```bash
python manage.py runserver
```

Abre:

```txt
http://127.0.0.1:8000/admin/
```

Inicia sesión con el superusuario.

Ahora deberías ver la sección `Productos`.

Desde ahí puedes:

- Crear productos.
- Editar productos.
- Eliminar productos.
- Ver la lista de productos.

---

# 14. Resumen de Comandos

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
python manage.py startapp productos
python manage.py makemigrations
python manage.py migrate
```

---

# 15. Flujo Recomendado para Clase

1. Explicar qué es un superusuario.
2. Crear el superusuario en vivo.
3. Entrar al panel admin.
4. Explicar los archivos del proyecto.
5. Crear la app `productos`.
6. Registrar la app en `settings.py`.
7. Crear una vista simple.
8. Crear `productos/urls.py`.
9. Conectar la app con `core/urls.py`.
10. Probar la ruta en el navegador.
11. Crear el modelo `Producto`.
12. Ejecutar migraciones.
13. Registrar el modelo en el admin.
14. Crear productos desde el panel administrativo.

---

# 16. Conclusión

En esta etapa ya tienes un proyecto Django funcional con:

- Superusuario creado.
- Panel administrativo funcionando.
- Archivos principales comprendidos.
- Primera aplicación creada.
- Primera ruta conectada.
- Primer modelo creado.
- Modelo visible desde el admin.

Este es el punto de partida para construir aplicaciones más completas con Django.