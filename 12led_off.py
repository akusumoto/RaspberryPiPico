import machine
import utime

print("Welcome to toggle external LED program v.0.02 (20231218)")

def led_on(pin):
    machine.Pin(pin, machine.Pin.OUT).value(1)

def led_off(pin):
    machine.Pin(pin, machine.Pin.OUT).value(0)

for i in range(12):
    led_off(i+10)
