# Django - Boilerplate para empezar proyectos nuevos

Ejecutar:
```docker-compose up```
DOCKER
Para usar tienen que tener instalado  docker y docker-compose, ver tutorial https://www.hostinger.es/tutoriales/instalar-docker-centos7
```yum install docker-ce
```
PYTHON
Dentro de la maquina de Python 3.8, se instala el django de la siguiente manera
```
pip install -r requirements.txt 
python manage.py migrate
python manage.py runserver

```
MYSQL 
Las credenciales y nombre de la base de datos se tienen que definir previamenteaen el archivo DockerFile 


```
 environment:
      - MYSQL_ROOT_PASSWORD=root1234
      - MYSQL_DATABASE=base

```
La maquina de MySQL se utiliza con datos persistentes tambien dentro del DockerFile, con la ruta hacia la base de datos local. 

```
    volumes:
      - ./mysql:/var/lib/mysql

```

Tambien tienen que tener bajo el mysql local, utilizando el comando: 

```
	systemctl stop mysql
```
TUTORAL DJANGP:

Para instalar, configurar y aprendar a usar DJANGO, ver el siguinte enlace: 
https://tutorial.djangogirls.org/es/
CONFIG DJANGO:
Para cargar la configuración de la conexion de proyecto con la base de datos tienen crear el archivo ./proyecto/local_settings, tiene uno de ejemplo ./proyecto/local_settings.php

## NOTA: No se deben subir al proyecto de git los archivos de configuración que contengan datos sensibles de usuario

```
cd ta2-django/proyecto
cp local_settings.py.ejemplo local_settings.py
cat local_settings.py


```
Contenido del local_settings
```
DEBUG = True
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'base',
        'USER': 'root',
        'PASSWORD': 'root1234',
        'HOST' : 'mysql',
    }
}
```

