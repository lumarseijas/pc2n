# MEMORIA PRÁCTICA CREATIVA 2

## GRUPO 24: Cristina Rodríguez Lozano, Elsa Sastre del Olmo y Lucía Martínez Seijas

---

## 1. Despliegue de la Aplicación en Máquina Virtual Pesada

Para el despliegue de la aplicación como monolito, se desarrolló un script llamado `p1.py` que automatiza el proceso de instalación y configuración. Este script realiza las siguientes tareas:

1. **Actualización del sistema**: Asegura que la máquina tenga los paquetes actualizados.
2. **Clonación del repositorio**: Clona el repositorio de la práctica que contiene el código de la aplicación.
3. **Instalación de dependencias**: Instala las dependencias especificadas en el archivo `requirements.txt` del proyecto usando `pip3`.
4. **Personalización del título**: Configura la variable de entorno `GROUP_NUM` con el valor `24` y modifica el archivo `productpage.html` para que el título de la aplicación incluya el número del grupo.
5. **Cambio de puerto de ejecución**: La aplicación, que por defecto escucha en el puerto `9080`, se ejecuta en un puerto configurable para adaptarse a diferentes configuraciones.
6. **Acceso externo**: La aplicación es accesible desde cualquier navegador mediante la IP pública y el puerto configurado: `http://<ip-pública>:<puerto>/productpage`.
7. **Liberación de recursos**: Permite liberar recursos eliminando los archivos generados durante el proceso.

### Ejecución
Para probar la funcionalidad, ejecutamos el script en la máquina con la IP local de nuestro ordenador. Utilizamos el siguiente comando:

```bash
python3 p1.py arrancar
```

En el navegador buscamos:

```text
http://<ip-local>:9080/productpage
```

La aplicación muestra correctamente la interfaz gráfica con el título: **"GRUPO 24"**.

---

## 2. Despliegue de una Aplicación Monolítica Usando Docker

Para desplegar la misma aplicación monolítica utilizada en la P1, empleamos contenedores Docker.

### Dockerfile
Se definió un fichero `Dockerfile` con las siguientes características:

- Usa como base la imagen `python:3.7.7-slim`.
- Instala dependencias necesarias como `git` y `pip3`.
- Clona el repositorio con el código de la aplicación.
- Configura la variable de entorno `GROUP_NUM` con el valor `24` para personalizar el título de la página.
- Expone el puerto `5060` y ejecuta la aplicación.

### Automatización
Se desarrolló un script (`p2.py`) que automatiza el proceso de construcción y ejecución del contenedor Docker con las siguientes funcionalidades:

1. **Construcción de la imagen Docker**: Usa el formato `productpage/24`.
2. **Ejecución del contenedor**:
   - Nombre: `productpage-24`.
   - Puerto: `5060`.
   - Variable de entorno: `GROUP_NUM=24`.
3. **Liberación de recursos**: Detiene y elimina contenedores e imágenes Docker al finalizar.

### Ejecución
El script fue ejecutado en una máquina local con Docker instalado, usando el siguiente comando:

```bash
python3 p2.py crear
```

En el navegador buscamos:

```text
http://<ip-local>:5060/productpage
```

La aplicación muestra correctamente la interfaz gráfica con el título personalizado.

