# Gestor de tareas en Python

Aplicación de consola desarrollada en Python para administrar tareas personales.

## Funcionalidades

- Agregar nuevas tareas.
- Listar todas las tareas.
- Marcar tareas como completadas.
- Guardar tareas en un archivo JSON.
- Cargar automáticamente las tareas guardadas al iniciar.
- Configuración global mediante el patrón de diseño Singleton.
- Pruebas unitarias con `unittest`.

## Estructura del proyecto

```text
gestor_tareas_python/
├── main.py
├── task_manager.py
├── config.py
├── tasks.json
├── README.md
├── .gitignore
├── capturas/
└── tests/
    └── test_task_manager.py
```

## Requisitos

- Python 3.10 o superior.
- No se requieren paquetes externos.

## Ejecución

Desde la carpeta del proyecto:

```bash
python main.py
```

En Windows también puede utilizarse:

```bash
py main.py
```

## Pruebas unitarias

Ejecutar:

```bash
python -m unittest discover -s tests -v
```

Las pruebas verifican principalmente que se puedan agregar tareas y marcar tareas como completadas.

## Patrón Singleton

La clase `Config` de `config.py` implementa Singleton mediante el método `__new__`. De esta forma existe una sola instancia de configuración para toda la aplicación. En ella se almacenan valores globales como `debug` y el nombre del archivo JSON.

## Persistencia JSON

La clase `TaskManager` carga las tareas desde `tasks.json` al inicializarse y guarda cambios después de agregar o completar una tarea. También se guarda nuevamente al cerrar desde el menú principal.

## Control de versiones

El proyecto fue preparado con al menos tres commits de ejemplo:

1. `Inicialización del proyecto y estructura básica.`
2. `Implementación del patrón Singleton.`
3. `Agregadas funciones para agregar, listar y completar tareas.`

## GitHub

Para entregar la actividad, crea un repositorio en GitHub, vincula este proyecto y realiza el `push`. Después copia la URL del repositorio en el documento Word de entrega.
