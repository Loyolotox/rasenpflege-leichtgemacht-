from machine import Pin
import time

led = Pin(2, Pin.OUT)

while True:
    led.value(0)  # an (invertiert)
    print("LED an")
    time.sleep(0.5)
    led.value(1)  # aus
    print("LED aus")
    time.sleep(0.5)
