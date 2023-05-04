#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.iodevices import UARTDevice

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# CONSTANTS
RAD2DEG = 57.2958
DEG2RAD = 0.017453
SYNC = bytes('X', 'utf-8')
R = bytes('R', 'utf-8')
L = bytes('L', 'utf-8')

# Useful variables
ref_L = 0
ref_R = 0

# Create your objects here.
ev3 = EV3Brick()

timer = StopWatch() # Set up the Timer.

mR = Motor(Port.D, Direction.COUNTERCLOCKWISE) 
mL = Motor(Port.A, Direction.COUNTERCLOCKWISE) 

uart = UARTDevice(Port.S1, 115200)


# Write your program here.

mR.speed()
mL.speed()

while True:
    timer.reset()

    #print(uart.waiting())

    while uart.waiting() >= 7:
        sync = uart.read()
        #print(sync)
        if(sync == SYNC):
            sync = uart.read()
            #print(sync)
            if sync == R:
                str_R = uart.read(5)
                try:
                    ref_R = float(str_R) / 100
                except:
                    #print("E")
                    pass
            if sync == L:
                str_L = uart.read(5)
                try:
                    ref_L = float(str_L) / 100
                except:
                    #print("E")
                    pass

    mR.run(ref_R * RAD2DEG)
    mL.run(ref_L * RAD2DEG)

    sR = int(mR.speed() * DEG2RAD * 100)
    sL = int(mL.speed() * DEG2RAD * 100)

    to_print = "wR{:05}wL{:05}".format(sR,sL)
    #print(to_print)
    uart.write(to_print)

    while timer.time() < 100:
        pass