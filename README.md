# LEGO EV3 programarlo con MicroPython

NOTA PRINCIPAL: Este el proceso que he seguido para poder utilizar el robot LEGO EV3 con MicroPython, ya tiene preparado un cable UART y la SD instalada en uno de los robots.

Objetivo: 
- Expandir las capacidades del LEGO EV3 con un cable UART. Con este cable podemos controlar el robot con un Arduino o Raspberry, siempre y cuando podemos montarlo en el robot. 
- Programar LEGO EV3 utilizando Python, específicamente MicroPython. Se puede cargar y descargar el código al robot via USB o WiFi mediante SSH con el editor de Visual Studio Code.

En la carpeta compressed_files_resources tienes todos los archivos necesarios comprimidos por partes, con un programa como 7zip puedes descomprimir estos archivos.

## Es necesario instalar un sistema operativo en una SD

El sistema operativo que vamos a emplear es la versión preparado por ev3dev. Existe otra versión proporcionado por LEGO, se basa en una versión aprobada por LEGO del sistema operativo ev3dev. (https://www.ev3dev.org/downloads/)

## Como hacer un cable para leer la UART del LEGO EV3
Se puede crear un cable para conectarlo directamente al PC. Puede ser muy útil para comprobar si está cargando correctamente el sistema operativo, también lo podemos ver en la pantalla del EV3. (3v3 TTL UART) 
- http://botbench.com/blog/2013/08/15/ev3-creating-console-cable/ (Backup en docs) 

Este cable también puede servir para comunicarse con MCU a 3V3 como podrían Arduino o ESP32 a través de un puerto UART.

## Ejemplos
- getting_started        -> Ejemplo muy sencillo de programación del Brick.
- getting_started_motors -> Ejemplo de control de los motores mediante un mensaje mandado por UART para establecer una velocidad en cada una de las ruedas.
- getting_started_uart   -> Ejemplo muy sencillo de programación y el uso de la UART. Además hay un ejemplo en Arduino para leer la UART del LEGO.

## Versión portable de Visual Studio Code con micropython

Se ha preparado una versión portable con los paquetes necesarios y vuelto a comprimir dividio en partes para poder ser subido al repositorio.
- https://code.visualstudio.com/docs/editor/portable

Es muy cómodo programarlo con VSCode.

## En compressed_files_resources puedes encontrar en formato comprimido por partes:
- Una versión de Visual Studio Code para Windows con el Micropython instalado -> VSCode-win32-x64-1.77.0-micropython
- Una versión de Balena Etcher para poder quemar la imagen de LEGO EV3 en una SD.
- La versión de EV3 generada por los EV3Dev -> ev3dev-stretch-ev3-generic-2020-04-10
- La versión de EV3 generada por LEGO -> ev3micropythonv200sdcardimage

## ESPECIAL comunicación WiFi

COMUNICATION WIFI CON LEGO EV3
- https://coolplaydev.com/socket-on-mindstorms-ev3
- https://pybricks.com/install/mindstorms-ev3/installation/

### Además de ejemplos con MQTT

https://www.ev3dev.org/docs/tutorials/sending-and-receiving-messages-with-mqtt/

## Véase todos los docs sino hay alguna página disponible, hay muchas copias de seguridad

## Links
- https://pybricks.com/ev3-micropython/index.html
- https://www.ev3dev.org/  
- https://www.ev3dev.org/docs/tutorials/
- https://www.ev3dev.org/downloads/
- http://botbench.com/blog/2013/08/15/ev3-creating-console-cable/ 
- https://education.lego.com/en-us/product-resources/mindstorms-ev3/teacher-resources/python-for-ev3/
- https://github.com/ev3dev/lego-linux-drivers/tree/ev3dev-stretch
