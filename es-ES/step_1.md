## Introducción

En este proyecto, crearás un tablero que visualizará los datos; puedes elegir qué datos mostrar de una variedad de fuentes en línea. Tu panel de datos deberá cumplir con el **resumen del proyecto**.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Un <span style="color: #0faeb0">tablero</span> es una interfaz de usuario que brinda un resumen actual de información importante, generalmente en forma gráfica o fácil de leer. El término se origina en los automóviles, donde al conductor se le muestra el estado actual del vehículo mediante diales y escalas grandes y brillantes.</p>

Vas a:
+ Construir indicadores automatizados usando motores y elementos LEGO®
+ Acceder a una **API** (interfaz de programación de aplicaciones) en línea para recuperar datos interesantes utilizando Python
+ Mostrar los datos elegidos en un tablero crado con LEGO

--- no-print ---

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1">

--- /no-print ---


--- collapse ---
---
title: Lo que necesitarás
---
### Hardware

+ Una computadora Raspberry Pi
+ Un Build HAT Raspberry Pi
+ Una fuente de alimentación Raspberry Pi Build HAT de 7.5V
+ 2 motores LEGO® Technic ™ (más opcionales)
+ Un sensor de fuerza LEGO® SPIKE ™
+ Surtido de LEGO® (utilizamos una selección del [LEGO® SPIKE ™ Prime](https://education.lego.com/en-gb/product/spike-prime){:target="_blank"})
+ Papel o cartulina
+ Tachuela o cinta adhesiva para pegar la tarjeta
+ Rotulador o lápiz
+ Tijeras o cuchillo artesanal

Opcional:
+ LED
+ Resistencias
+ Cables de puente
+ Una placa de pruebas
+ Pernos y tuercas M2 (× 2 de cada uno para montar la Raspberry Pi en la placa de construcción LEGO®)

### Software

+ Biblioteca BuildHAT Python para controlar Build HAT
+ IDE de Thonny Python

### Descargas

+ El programa final de este proyecto está disponible [aquí]((https://rpf.io/p/es-ES/lego-data-dash-go){:target="_blank"})

--- /collapse ---

Antes de comenzar, deberás configurar tu computadora Raspberry Pi e instalar el Build HAT:

--- task ---

Monta tu Raspberry Pi en la placa de construcción LEGO usando pernos y tuercas M2, asegurándote de que la Raspberry Pi esté en el lado sin el 'borde':

 ![Raspberry Pi atornillada a una placa de construcción LEGO magenta.](images/build_11.jpg)

--- /task ---

Montar la Raspberry Pi de esta manera permite un fácil acceso a los puertos, así como a la ranura de la tarjeta SD. La placa de construcción te permitirá conectar la Raspberry Pi a la estructura principal de tu tablero más fácilmente.

--- task ---

Alinea el Build HAT con la Raspberry Pi, asegurándote de que puedes ver la etiqueta `This way up`. Asegúrate de que todos los pines GPIO estén cubiertos por el HAT y presiona firmemente. (El ejemplo usa un encabezado de apilamiento [](https://www.adafruit.com/product/2223){:target="_blank"}, lo que alarga los pines)

![Imagen de los pines GPIO asomándose por la parte superior del Build HAT.](images/build_15.jpg) ![Animación que muestra el ajuste de Buildhat a Raspberry Pi](images/haton.gif)

--- /task ---

Ahora debes encender tu Raspberry Pi utilizando el conector de barril de 7.5V en el Build HAT, lo cual te permitirá usar los motores.

--- task ---

Si aún no lo ha hecho, configura tu Raspberry Pi siguiendo estas instrucciones:

[Configurando tu Raspberry Pi](https://projects.raspberrypi.org/es-ES/projects/raspberry-pi-setting-up){:target="_blank"}

--- /task ---

--- task ---

Una vez que la Raspberry Pi se haya iniciado, abra la herramienta de configuración de Raspberry Pi haciendo clic en el botón Menú de Raspberry y luego seleccionando "Preferencias" y luego "Configuración de Raspberry Pi".

Haz clic en la pestaña "interfaces" y ajusta la configuración Serie como se muestra a continuación:

![Imagen que muestra la pantalla de configuración del sistema operativo Raspberry Pi con el puerto en serie habilitado y la consola en serie deshabilitada](images/configshot.jpg)

--- /task ---

--- task ---

También necesitarás instalar la biblioteca buildhat de python siguiendo estas instrucciones:

--- collapse ---
---
title: Instale la biblioteca buildhat Python
---

Abre una ventana de terminal en tu Raspberry Pi presionando <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>T</kbd>.

En el indicador, escribe: `sudo pip3 install buildhat`

Presiona <kbd>Entrar</kbd> y espera el mensaje "installation completed".

--- /collapse ---

--- /task ---


<div style="border-top: 15px solid #f3524f; background-color: whitesmoke; margin-bottom: 20px; padding: 10px;">

### RESUMEN DEL PROYECTO: Panel de datos LEGO®
<hr style="border-top: 2px solid black;">

Tu tarea es crear un tablero de LEGO que mostrará los datos elegidos. Las fuentes para tus datos pueden ser cualquier API que quieras, pero en este ejemplo, te mostraremos cómo acceder a OpenAQ, que requiere mínimo o ningún registro. 

Para nuestros datos de ejemplo, mediremos:
+ Los niveles de **NO2** en una ubicación elegida. El dióxido de nitrógeno (NO2) es uno de un grupo de gases altamente reactivos conocidos como óxidos de nitrógeno o NOx. El NO2 se libera principalmente al aire a partir de la quema de combustible.
+ Los niveles de **partículas finas (PM2.5)** en una ubicación elegida. El término **partículas finas**, o material particulado 2.5 (PM2.5), se refiere a partículas diminutas o gotitas en el aire que tienen un tamaño de dos micrones y medio (o menos). Las partículas clasificadas como PM2.5 son las que forman el humo y el smog.


<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">La API de ejemplo que estamos usando en este proyecto es de [OpenAQ](https://openaq.org/#/), una organización global sin fines de lucro que "lucha contra la desigualdad del aire a través de datos abiertos". A nivel mundial, **1 de cada 8 muertes** se debe a la mala calidad del aire, y OpenAQ recopila datos sobre la calidad del aire a nivel mundial para ayudar a informar a más personas sobre los problemas del aumento de la contaminación del aire en algunas partes del mundo. </p>


Tu tablero debe:
+ Usar LEGO® para mostrar los datos elegidos de una manera clara
+ Acceder a una API en línea para recuperar datos actualizados
+ Tener al menos dos indicadores LEGO®

Tu tablero podría:
+ Usar otros componentes electrónicos (LED, zumbadores)
+ Tener entradas físicas del usuario (motores LEGO® Technic ™, sensor de fuerza LEGO®, botón GPIO, sensor de distancia)
  
</div>

--- no-print ---

### Inspírate

--- task ---

Piensa qué información te gustaría mostrar en tu tablero mientras investigas estos proyectos de ejemplo para obtener más ideas.

Este ejemplo muestra un tablero meteorológico que muestra la temperatura actual en un control deslizante vertical, la nubosidad usando una escala LED y en los diales giratorios sugiere un nivel adecuado de ropa basado en la temperatura aparente (incluye el viento y otras condiciones climáticas en el temperatura) y un informe meteorológico detallado utilizando los códigos meteorológicos mundiales (también conocidos como Código OMM).

![Vídeo de demostración](images/weather-dash.gif)

--- /task ---

--- /no-print ---

--- print-only ---

![Imagen que muestra el tablero de una estación meteorológica hecho de LEGO®.](images/example-dash.jpg)

--- /print-only ---


