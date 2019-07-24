# BlaBla v1.0.0

En el marco de [Programa de Voluntarios](http:/ciencia.chubut.gov.ar/programa-de-voluntarios/) dearrollamos un comunicador por pictogramas de interface simple pensado en un principio para ser utilizado con seguidores de pupila de escaza resolución como Gaze Pointer. El uso requiere asistencia del terapeuta y por el momento no despliega opciones linkeadas.

## Comenzando 

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo, pruebas y uso final._


### Pre-requisitos

* El software fue desarrollado para funcionar en **Windows 10** ya que por el momento es el estandar en los centros de rehabilitación y en las computadoras personales de las familias que lo implementarían. 

* Recomendamos la instalción de [GazePointer](https://sourceforge.net/projects/gazepointer/) y su calibración (puede guardarse para usos futuros en sitiaciones similares)


### Instalación 

1. Descarga o clona este respositorio dentro de la carpeta _Build_ vas a encontrar la versión ejecutable

2. Carga las imagenes que quieres usar de pictogramas en las carpetas dentro de _diapos_ el numero de carpeta corresponde a una diapositiva. Las imagenes deben tener un tamaño de 300x300 px. En cada caperta puede ponerse solo los siguientes numeros de imagenes, cualquier otro numero probocará la detención del programa:
  0 arvhicos -> no se carga la diapositiva
  2 archivos -> diapositiva con grilla dos pictogramas
  4 archivos -> diapositiva con grilla de 4 pictogramas

3. Renombra los archivos de imagenes con la locución correspondiente, podes usar _'_'_ para los espacios o simplemente espacio, por ejemplo el pictograma de una escuela puede renombrarse a _'quiero ir a la escuela.jpg'_ o _'quiero_ir_a_la_escuela.jpg'_ 

4. Ejecuta y calibra GazePointer seleccionando la opción para controlar el puntero.

5. Ejecuta blabla.exe


## Deployment 📦

* El software fué desarollado en Python 3 y requiere [PyGame](https://www.pygame.org/wiki/GettingStarted)

## Construido con 🛠️

_Menciona las herramientas que utilizaste para crear tu proyecto_

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - El framework web usado
* [Maven](https://maven.apache.org/) - Manejador de dependencias
* [ROME](https://rometools.github.io/rome/) - Usado para generar RSS

## Contribuyendo 🖇️

Por favor lee el [CONTRIBUTING.md](https://gist.github.com/villanuevand/xxxxxx) para detalles de nuestro código de conducta, y el proceso para enviarnos pull requests.


## Versionado 📌

Usamos [SemVer](https://semver.org/lang/es/) para el versionado. 

## Autores ✒️

_Menciona a todos aquellos que ayudaron a levantar el proyecto desde sus inicios_

* **Antonio Armada** - *Trabajo Inicial* 

También puedes mirar la lista de todos los [contribuyentes](https://github.com/your/project/contributors) que participaron en este proyecto. 

## Licencia 📄

Este proyecto está bajo la Licencia (Tu Licencia) - mira el archivo [LICENSE.md](LICENSE.md) para detalles

## Expresiones de Gratitud 🎁

* Comenta a otros sobre este proyecto 📢
* Invita una cerveza 🍺 a alguien del equipo. 
* Da las gracias públicamente 🤓.
* etc.



---
⌨️ con ❤️ por [Villanuevand](https://github.com/Villanuevand) 😊
