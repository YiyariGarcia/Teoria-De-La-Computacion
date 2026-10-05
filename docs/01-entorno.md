# Paso A
## Investigacion  

1. **¿Que es un sistema de control de versiones y que problema resuelve en un trabajo en equipo?**  

   * Es una practica importante de desarrollo de software para hacer un seguimiento y gestionar los cambios realizados al codigo y a otros archivos.  Para un trabajo en equipo ayuda muchisimo a saber quien realizo cada cambio, poder volver a corregirlo o arreglar algun error sin necesidad de que ambos esten conectados simultaneamente, cada quyien puede entrar y saber que hizo o modifico el otro mediante el historial de versiones y los comentrarios o el resumen que dejan de los cambios hechos o las correcciones. Ademas, pueden dividirse el trabajo sin necesidad de hacer dobles archivos, todos trabajando en un mismo archivo simultaneamente.  

2. **¿Cual es la diferencia entre Git y GitHub?**
   * Basicamente Git es la base donde se hace el control de versiones, guarda el historial y permite regresar a una version anterior, todo eso localmente, mientras que Github es un servicio en la nube, aloja los repositorios que se crean con Git y añade las funciones para el trabajo en equipo online (Git no necesita internet y GitHub si necesita internet).  

3. **Defina, con sus palabras y con un ejemplo:**
   * **Repositorio:** Es la carpeta donde se guardan todos los archivos y codigos que se hacen con Git.
   * **Commit:** El commit es la confirmacion de la edicion o de la correccion enb los archivos, digamos que es un punto de guardado.
   * **Branch:** Las branch son una linea paralela, donde alguien mas puede hacer modificaciones al proyecto, pero sin alterar el proyecto main o la main branch.
   * **Merge:** Basicamente es la fusion entre la main branch y las demas branch.
   * **Conflicto de fusion:** Un conflicto de fusion ocurre cuando hay commits que se modificaron la misma linea, al mismo tiempo de diferentes branchs y ahi en ese sentido te pide confirmar que version deseas guardar.
   * **Pull Request:** El Pull request es basicamente una buena practica para trabajar en equipo con GitHub, basicamente es una solicitud para fusiuonar tu branch con la main branch, donde tu y el equipo revisan tu trabajo para ver si si esta bien o estan de acuerdo con ese cambio y si estan de acuerdo se hace la fusion.
   * **Archivo `.gitignore`:** Es el archivo que pertenece al repositorio de Git que le especifica a Git que carpetas, archivos o lineas debe de ignorar, no debe de subir y no debe de rastrear.
   * **Archivo `README`:** Es la carta de presentacion o la portada de tu proyecto, es el primer archivo que muestra Git por default.  

4. **¿Que es un contenedor y en que se diferencia de una maquina virtual, en cuanto a arranque, tamaño y aislamiento?**
   * **Contenedor:** es un software de paquete ligero, ejecutable y autonomo que incluye todo lo necesario paraq ue una aplicacion funcione. Su proposito principal es resolver el tipico problema de "funciona en mi maquina, pero no en produccion".
   * **Diferencias:**  
      * **Arranque:** Maquina virtual tarda varios minutos, mientras que el contenedor tarda milisegundos o pocos segundos.
      * **Tamaño:** La maquina virtual pesa Gb (Gigabytes) lo cual es pesadisimo, mientras que el contenedor pesa Mb (megabytes) lo cual es muy ligero.
      * **Aislamiento:** La maquina virtual hace un Hardware virtualizado, mientras que el contenedor usa un kernel del software.  

5. **Defina: imagen, contenedor, volumen y puerto publicado**
   * **Imagen:** Es una plantilla de solo lectura que empaqueta el codigo fuente, dependencias, librerias y configuraciones necesarias para ejecutar una aplicacion.
   * **Contenedor:** Es un entorno de proceso aislado dentro del SO anfitrion que ejecuta la aplicacvion de forma ligera y autonoma.
   * **Volumen:** Es un almacenamiento alojado en el sistema anfitrion. Permite guardar datos fuera del ciclo de vida del contenedor, evitando que la informaciuon se pierda cuando el contenedor se detiene, elimina o actualiza.
   * **Puerto Publicado:** Redireccion de red que vincula un puerto del host con un puerto interno del contenedor y permite exponer los servicios aislados del contenedor para que pueda ser accesible desde fuera de el.  

6. **¿Que es un entorno virtual de Python y por que un entorno virtual no modifica la version del interprete?**
   * Un entorno virtual de Python es un directorio aislado que contiene su propia version del interprete de Python y su propio conjunto de bibliotecas instaladas, independiente de la instalaciuon global del sistema o de otros proyectos.
   Los entornos virtuales no modifican la version del interprete porque, la herramienta (`venv`) no instala una nueva copiua completa ni altera el codigo del SO. En su lugar, crea un enlace simbolico que apunta hacia el ejecutable especifico de Python con el que fue creado, tambien el proposito de que sea un entorno virtual es aislar unicamente el espacio de librerias y dependencias, asegurando que las instalaciones no afecten la instalacion global de Python no interrumpan otros proyectos o herramientas del sistema.  
7. **¿Por que conviene fijar la version de la imagen, `python:3.12-slim`, en lugar de emplear `python:latest`.**
   * La etiqueta `latest` es flotante, lo que significa que cambia dinamicamente cada vez que se publica una nueva version de python y esto podria ocasionar fallos inesperados, como romper dependencias, cambiando funciones obsoletas o generando fallos no detectados en tu codigo. Ademas, la variante `3:12-slim` elimina software innecesario, reduciendo el peso y esto acelera las descargas y el tiempo de arranque. Si todo esto no era aun suficiente, como la variante `3:12-slim` contiene una menor cantidad de paqueterias y librerias del sistema operastivo, esto reduce drasticamente la cantidad de vulnerabilidades conocidas y expone mucho menos herramientas de las que podian aprovecharse.  
   Basicamente fijar la variante `3:12-slim` garantiza que el codigo se ejecute en el mismo entorno de ejecucion exacto sin importar quien o donde se construya el contenedor.