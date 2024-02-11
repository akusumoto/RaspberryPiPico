from machine import Pin
import utime

led = Pin("LED", Pin.OUT)
while True:
    led.toggle()
    utime.sleep(1)