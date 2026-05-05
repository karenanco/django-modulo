# 🚀 Proyecto Django 6.0 - Guía de Instalación

Este documento describe paso a paso cómo configurar el entorno de desarrollo e iniciar un proyecto utilizando **Django 6.0**.

---

## 📌 1. Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:

- **Python 3.10 o superior**
- **pip**: gestor de paquetes de Python

Puedes verificar las versiones instaladas con:

```bash
python --version
pip --version
```

---

## 🧱 2. Entorno Virtual

El entorno virtual, también conocido como `venv`, permite crear un espacio aislado para instalar las librerías del proyecto.

### ¿Para qué sirve?

Sirve para evitar conflictos entre versiones de librerías de diferentes proyectos.

Por ejemplo:

- Un proyecto puede usar Django 5.0.
- Otro proyecto puede usar Django 6.0.

Gracias al entorno virtual, ambos proyectos pueden existir en la misma computadora sin interferir entre sí.

---

## ⚙️ 3. Crear el Entorno Virtual

Desde la carpeta raíz del proyecto, ejecuta:

```bash
python -m venv venv
```

Esto creará una carpeta llamada `venv/`.

---

## ▶️ 4. Activar el Entorno Virtual

### En Windows

```bash
.\venv\Scripts\activate
```

### En Linux o macOS

```bash
source venv/bin/activate
```

Cuando el entorno virtual esté activado, normalmente verás algo como esto al inicio de la terminal:

```bash
(venv)
```

---

## 📦 5. Archivo de Dependencias

Crea un archivo llamado:

```txt
requirements.txt
```

Este archivo debe estar ubicado en la raíz del proyecto.

Su función es guardar todas las librerías necesarias para que el proyecto funcione correctamente.

---

## 📄 6. Contenido del archivo requirements.txt

```txt
# Framework principal
Django==6.0

# Manejo de variables de entorno
python-decouple==3.8

# Conector de base de datos PostgreSQL
psycopg2-binary==2.9.9

# Extensiones útiles para desarrollo
django-extensions==3.2.3

# Servidor de aplicaciones para producción
gunicorn==21.2.0
```

---

## 📚 7. Explicación de las Librerías

### Django

Es el framework principal que se usará para crear la aplicación web.

```txt
Django==6.0
```

Permite trabajar con:

- Rutas
- Vistas
- Modelos
- Formularios
- Autenticación
- Panel de administración
- Base de datos

---

### python-decouple

```txt
python-decouple==3.8
```

Permite separar configuraciones sensibles del código fuente.

Por ejemplo:

- Llaves secretas
- Contraseñas
- Configuración de base de datos
- Variables de entorno

Normalmente se usa junto con un archivo `.env`.

---

### psycopg2-binary

```txt
psycopg2-binary==2.9.9
```

Es el conector que permite que Django pueda comunicarse con una base de datos PostgreSQL.

En desarrollo se puede usar SQLite, pero para producción se recomienda PostgreSQL.

---

### django-extensions

```txt
django-extensions==3.2.3
```

Agrega comandos adicionales útiles al archivo `manage.py`.

Por ejemplo:

- Herramientas para visualizar modelos
- Shell mejorado
- Comandos extra para desarrollo

---

### gunicorn

```txt
gunicorn==21.2.0
```

Es un servidor de aplicaciones utilizado normalmente en producción.

Se usa para ejecutar proyectos Django en servidores reales.

---

## ⚙️ 8. Instalar Dependencias

Primero, asegúrate de tener el entorno virtual activado.

Luego ejecuta:

```bash
pip install --upgrade pip
```

Después instala las dependencias:

```bash
pip install -r requirements.txt
```

---

## 🏗️ 9. Crear el Proyecto Django

Con las dependencias instaladas, ejecuta:

```bash
django-admin startproject core .
```

El punto `.` al final es importante.

Indica que Django debe crear los archivos del proyecto en la carpeta actual, evitando crear una subcarpeta innecesaria.

---

## 📁 10. Estructura Inicial del Proyecto

Después de ejecutar el comando anterior, la estructura será similar a esta:

```txt
proyecto/
│
├── venv/
├── requirements.txt
├── manage.py
│
└── core/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

---

## 🗄️ 11. Ejecutar Migraciones Iniciales

Django incluye por defecto aplicaciones internas como:

- Usuarios
- Sesiones
- Permisos
- Administración

Estas aplicaciones necesitan crear tablas en la base de datos.

Para hacerlo, ejecuta:

```bash
python manage.py migrate
```

---

## ▶️ 12. Ejecutar el Servidor de Desarrollo

Para iniciar el servidor local de Django, ejecuta:

```bash
python manage.py runserver
```

Luego abre el navegador y entra a:

```txt
http://127.0.0.1:8000/
```

Si todo está correcto, verás la página inicial de Django.

---

## 📌 13. Resumen de Archivos Generados

| Archivo / Carpeta | Función |
|---|---|
| `venv/` | Contiene el entorno virtual con Python y las librerías instaladas. |
| `requirements.txt` | Lista de dependencias necesarias para ejecutar el proyecto. |
| `manage.py` | Herramienta de línea de comandos para interactuar con Django. |
| `core/settings.py` | Archivo principal de configuración del proyecto. |
| `core/urls.py` | Archivo donde se definen las rutas principales del proyecto. |
| `core/asgi.py` | Configuración para servidores ASGI. |
| `core/wsgi.py` | Configuración para servidores WSGI. |

---

## ✅ 14. Comandos Principales

```bash
python -m venv venv
```

```bash
.\venv\Scripts\activate
```

```bash
pip install --upgrade pip
```

```bash
pip install -r requirements.txt
```

```bash
django-admin startproject core .
```

```bash
python manage.py migrate
```

```bash
python manage.py runserver
```

---

## 💡 15. Recomendaciones

- No subir la carpeta `venv/` al repositorio.
- Crear un archivo `.gitignore`.
- Usar un archivo `.env` para guardar configuraciones sensibles.
- Mantener actualizado el archivo `requirements.txt`.
- Usar PostgreSQL para entornos de producción.

---

## 🧑‍💻 Autor

Documentación base para iniciar un proyecto con **Django 6.0**.