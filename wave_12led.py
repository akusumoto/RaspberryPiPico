"""
Wave 12 LEDs
using GP10 to GP21 (12 pins)
"""

import machine
import utime

print("Welcome to toggle external LED program v.0.02 (20231218)")

N_LED = 12
PIN_BASE = 10

def led_on(pin):
    machine.Pin(pin, machine.Pin.OUT).value(1)

def led_off(pin):
    machine.Pin(pin, machine.Pin.OUT).value(0)

def set_led(value):
    for i in range(N_LED):
        pin = i + PIN_BASE
        val = value & (0x01 << i)
        if val > 0:
            led_on(pin)
        else:
            led_off(pin)

value = 0x01
while True:
    set_led(value)    
    value = value << 0x01
    if value > 0x800:
        value = 0x01
    utime.sleep(0.02)

