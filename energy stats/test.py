import time
import os
import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
hallpin = 2
gpio.setup(hallpin, gpio.IN)

while True:
    if(gpio.input(hallpin) == 1):
        print("Detected")
    else:
        print("not detected")