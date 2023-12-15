# LEGO EV3 programarlo con micropython

Objetivo: 
- Expandir las capacidades del LEGO EV3 con un cable UART. 
- Programar LEGO EV3 utilizando Python, específicamente MicroPython.

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

## Links
- https://pybricks.com/ev3-micropython/index.html
- https://www.ev3dev.org/  
- https://www.ev3dev.org/downloads/ (Backup visual .pdf en docs)
- http://botbench.com/blog/2013/08/15/ev3-creating-console-cable/ (Backup visual .pdf en docs)
- https://education.lego.com/en-us/product-resources/mindstorms-ev3/teacher-resources/python-for-ev3/ (Backup visual .pdf en docs)

## Resumen ChatGPT

Pasos y componentes principales:

1. Instalar un sistema operativo preparado por ev3dev en el LEGO EV3, disponible en https://www.ev3dev.org/downloads/ (Recomendable). O la versión en la página de LEGO, según gusto.
2. Para leer el proceso de boot del LEGO EV3, se puede crear un cable UART (3v3 TTL UART) y conectarlo al PC. El proceso de construcción del cable se describe en http://botbench.com/blog/2013/08/15/ev3-creating-console-cable/.
3. El cable UART también puede utilizarse para la comunicación con otros dispositivos a 3.3V, como Arduino o ESP32.
4. Ejemplos de programas:
getting_started: Un ejemplo simple de programación del Brick.
getting_started_motors: Control de los motores mediante mensajes UART para establecer la velocidad de las ruedas.
getting_started_uart: Ejemplo básico de programación y uso de UART. También incluye un ejemplo en Arduino para leer la UART del LEGO.
5. Se proporciona una versión portable de Visual Studio Code con MicroPython instalado para facilitar la programación. Está dividida en partes.
6. Se proporcionan enlaces a recursos adicionales, como la documentación de Pybricks, ev3dev, y la página de descargas de ev3dev.

En resumen, el proyecto busca mejorar las capacidades de LEGO EV3 mediante la programación en MicroPython, utilizando un cable UART para la conexión y facilitando el proceso con una versión portable de Visual Studio Code. También se proporcionan enlaces a recursos adicionales para referencia y soporte.