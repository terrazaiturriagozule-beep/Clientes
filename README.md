# API de Gestión de Clientes

# Información general

Este proyecto corresponde a la elaboración de una API sencilla desarrollada con FastAPI.  
La finalidad principal es permitir la visualización de información relacionada con un proyecto y mostrar un listado de clientes utilizando diferentes rutas o endpoints.

# Inicio del proyecto

Como primer paso, se creó una carpeta llamada `nombre_pro_clientes` en el escritorio.  
Posteriormente, dicha carpeta fue abierta desde Visual Studio Code para comenzar el desarrollo de la aplicación.

# Configuración del entorno virtual

Una vez dentro de Visual Studio Code, se abrió la terminal integrada y se ejecutó el siguiente comando para generar el entorno virtual:

py -m venv yober

Este comando crea un entorno aislado llamado `Zule`, el cual permite instalar paquetes y dependencias sin modificar la instalación principal de Python.

# Habilitación del entorno virtual

Después de generar el entorno virtual, se procedió a activarlo utilizando el siguiente comando:

.\yober\Scripts\activate

Cuando la activación se realiza correctamente, el nombre `(Zule)` aparece al inicio de la consola, indicando que el entorno ya se encuentra en funcionamiento.

# Instalación del framework FastAPI

Con el entorno virtual activo, se realizó la instalación de FastAPI mediante el siguiente comando:

pip install "fastapi[standard]"

Esta instrucción instala el framework junto con las herramientas y dependencias necesarias para ejecutar correctamente la API.

# Comprobación de dependencias instaladas

Al finalizar la instalación, se utilizó el siguiente comando para revisar los paquetes instalados dentro del entorno virtual:

pip list

Gracias a este comando se pudo confirmar que FastAPI había sido instalado de manera correcta.

# Creación del archivo principal

Posteriormente se creó el archivo principal llamado `main.py`, el cual contiene la lógica principal de la API y la definición de los endpoints.

Las primeras líneas agregadas fueron:

from fastapi import FastAPI 

app = FastAPI()

# Explicación

`from fastapi import FastAPI`  
Esta línea se encarga de importar la clase FastAPI necesaria para construir la aplicación web.

`app = FastAPI()`  
Permite crear e inicializar la aplicación principal sobre la cual funcionará toda la API.

# Desarrollo de endpoints

@app.get("/proyecto")

def mensaje():
    return {"proyecto": "este es el proyecto de clientes a desarrollar"}

# Explicación

Este endpoint crea la ruta `/proyecto`.  
Cuando un usuario accede a dicha dirección, la API devuelve una respuesta en formato JSON con información relacionada al proyecto.

# Endpoint de clientes

lista= ["Yoberson","William","Suns","daniela","kamila","Quiroga"]

@app.get("/clientes")
def personas():
    return {"clientes": lista}

# Explicación

Este endpoint genera la ruta `/clientes`, cuya función es retornar una lista de clientes almacenados previamente dentro de una variable.

# Ejecución de la API

Para poner en funcionamiento la API se utilizó el siguiente comando:

fastapi dev main.py

# Resultado obtenido

Después de ejecutar el proyecto, la API quedó disponible de manera local en la siguiente dirección:

http://127.0.0.1:8000

# Rutas disponibles

- `/proyecto`
- `/clientes`