# Pokemon app

### Requirements
Esta aplicación se desarrolló en python 3.7.

Para instalar las dependencias se puede ejecutar el siguiente comando estando en el directorio raíz del proyecto:
```
pip install -r requirements.txt
```

## Ejecución del servicio
Estando en el directorio raíz, para ejecutar la app se pueden utilizar dos comandos:


```
python manage.py runserver
```
ó

```
gunicorn -w 1 -b 0.0.0.0:5000 "pokemon:create_app()"
```


### Install Pre-commit
Éste proyecto utiliza una herramienta de pre-commit, la cual re-ordena el codigo, verifica docstrings, imports, etc.

En modo dev, debemos instalar sus dependencias con el comando:

```
pip install -r requirements-dev.txt
```

y luego debemos activar el pre-commit con el comando:

```
pre-commit install
```