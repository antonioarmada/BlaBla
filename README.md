# BlaBla v1.0.1

En el marco de [Programa de Voluntarios](http:/ciencia.chubut.gov.ar/programa-de-voluntarios/) dearrollamos un comunicador por pictogramas de interface simple pensado en un principio para ser utilizado con seguidores de pupila de escaza resolución como Gaze Pointer. El uso requiere asistencia del terapeuta y por el momento no despliega opciones linkeadas.

Este software está siendo probado en el Servicio de Rehabilitación Psicomotora del Hospital de Trelew

## Cambios de versión

* Se agregó reescalado de imágenes automático a 300px por el proporcional de altura.

## Comenzando 

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo, pruebas y uso final._


### Pre-requisitos

* El software fue desarrollado para funcionar en **Windows 10** ya que por el momento es el estandar en los centros de rehabilitación y en las computadoras personales de las familias que lo implementarían. 

* Recomendamos la instalción de [GazePointer](https://sourceforge.net/projects/gazepointer/) y su calibración (puede guardarse para usos futuros en sitiaciones similares)


### Instalación 

1. Descarga o clona este respositorio 
2. Carga las imagenes que quieres usar de pictogramas en las carpetas que vas a encontrar dentro de _diapos_, el numero de carpeta corresponde a cada diapositiva. Las imágenes deben tener un tamaño de 300x300 px. En cada caperta puede ponerse solo los siguientes números de imágenes, cualquier otro número probocará la detención del programa:
   * 0 arvhicos -> no se carga la diapositiva 
   * 2 archivos -> diapositiva con grilla dos pictogramas
   * 4 archivos -> diapositiva con grilla de 4 pictogramas

3. Renombra los archivos de imágenes con la locución correspondiente, podes usar _"_"_ para los espacios o simplemente espacio, por ejemplo el pictograma de una escuela puede renombrarse a _'quiero ir a la escuela.jpg'_ o _'quiero_ir_a_la_escuela.jpg'_ 

4. Ejecuta y calibra GazePointer seleccionando la opción para controlar el puntero.

5. Ejecuta blabla.exe que está dentro de la carpeta _dist_


## Deployment

* El software fué desarollado en Python 3 y requiere [PyGame](https://www.pygame.org/wiki/GettingStarted)

## Construido con 

* [Python](https://www.python.org/download/releases/3.0/) - Lenguaje usado
* [PyGame](https://www.pygame.org/wiki/GettingStarted) - Librería para el desarrollo de juegos gráficos en Python

## Contribuyendo 

Por favor lee el [CONTRIBUTING.md](https://github.com/antonioarmada/BlaBla/blob/master/CONTRIBUTING.md) para detalles de nuestro código de conducta.


## Versionado 

Usamos [SemVer](https://semver.org/lang/es/) para el versionado. 

## Autores 

* **Antonio Armada** - _Desarrollo Inicial_
* **Viana Rossi** - _Tester_
* **Yanina Cascon** - _Tester_

También puedes mirar la lista de todos los [contribuyentes](https://github.com/your/project/contributors) que participaron en este proyecto. 

## Licencia 

Este proyecto está bajo la siguiente lincencia Creative Commons:

_“Atribución – No Comercial – Compartir Igual (by-nc-sa): No se permite un uso comercial de la obra original ni de las posibles obras derivadas, la distribución de las cuales se debe hacer con una licencia igual a la que regula la obra original. Esta licencia no es una licencia libre.”_


## Expresiones de Gratitud 

* Comentá a otros sobre este proyecto 
* Invitale una cerveza a alguien del equipo. 
* Dale las gracias públicamente.
* etc.



---

