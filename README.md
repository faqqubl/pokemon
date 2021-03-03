# Pokemon app

### Requirements
Esta aplicación se desarrolló en python 3.7 (Es recomendable tener creado un entorno virtual -> https://www.freecodecamp.org/news/virtualenv-with-virtualenvwrapper-on-ubuntu-18-04/).

Para instalar las dependencias se puede ejecutar el siguiente comando estando en el directorio raíz del proyecto:
```
pip install -r requirements.txt
```

### Ejecución del servicio
Estando en el directorio raíz, para ejecutar la app se pueden utilizar dos comandos:


```
python manage.py runserver
```
ó

```
gunicorn -w 1 -b 0.0.0.0:5000 "pokemon:create_app()"
```


### Install Pre-commit (DEV MODE)
Éste proyecto utiliza una herramienta de pre-commit, la cual re-ordena el codigo, verifica docstrings, imports, etc.

Si estamos en modo dev queriendo contribuir al proyecto, debemos instalar sus dependencias con el comando:

```
pip install -r requirements-dev.txt
```

y luego debemos activar el pre-commit con el comando:

```
pre-commit install
```


### Ejecución de Unit test

Estando en el directorio raìz, para ejecutar los unittest podemos hacerlo de dos formas:

1) Utilizando el comando: ```python setup.py test```
2) Instalando las dependencias de los tests con el comando ```pip install -r requirements-test.txt``` y luego ejecutando el comando ```pytest tests/```


### Endpoints predefinidos para la aplicación

1) Ejemplo de endpoint para obtener pokemons por parametros (nombre, limite y offset): ```http://0.0.0.0:5000/api/pokemon?q=saur&limit=11&offset=0```

2) Ejemplo de endpoint para obtener pokemons por nombre: ```http://0.0.0.0:5000/api/pokemon/charizard```
