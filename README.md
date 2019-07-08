# TODOList

## Aplicación para manejar una lista de tareas

TODOList es una mini aplicación web para el manejo de una lista de tareas. 

La aplicación actualmente se encuentra en el siguiente [link de acceso](https://todominiapp.herokuapp.com).

Está desarrollada en Django 2.1 y tiene las siguientes funcionalidades:

* Registrar usuarios
* Iniciar sesión con un usuario
* Cerrar sesión
* Obtener la lista de tareas y su estado actual
* Agregar tareas nuevas
* Editar tareas existentes
* Marcar tareas como completadas
* Eliminar tareas existentes

## Instalación

Primero asegúrese de instalar:

* PostgreSQL (11.4)
* Virtualenv (15.1.0)
* Python (3.7.3)
* pip (19.1.1)

### Configuración de un entorno virtual

Cree un nuevo entorno virtual en la carpeta del proyecto con python3 por defecto:

```
virtualenv env --python=$(which python3)
```

Para activar el entorno:
```
source env/bin/activate
```

Para desactivar el entorno:
```
deactivate
```

Para instalar los paquetes necesarios:
```
pip install -r requirements.txt
```

### Configuración de la base de datos / migraciones

Para configurar la base de datos se tiene el script `createdb.sh` y para aplicar las migraciones `migrate.sh`.

Para otorgar los permisos necesarios de ejecución:
```
chmod +x createdb.sh migrate.sh
```

Ahora para configurar la base de datos, ejecute:
```
./createdb.sh
```

Y para aplicar las migraciones y actualizar la base de datos:
```
./migrate.sh
```