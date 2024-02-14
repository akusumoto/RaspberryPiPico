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
    set_led(0x001)
    utime.sleep(1)
    set_led(0x800)
    utime.sleep(1)


