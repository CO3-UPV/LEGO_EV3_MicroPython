#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.iodevices import UARTDevice


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

uart = UARTDevice(Port.S1, 115200)

# Write your program here.
ev3.speaker.beep()

uart.write(b'\r\nHello, world!\r\n')

for i in range(10):
    print("Bytes waiting to be read:", uart.waiting())
    wait(1000)

# Read all data received while the sound was playing
data = uart.read_all()
print(data)