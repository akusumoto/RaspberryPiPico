import machine
import utime

print("Welcome to toggle external LED program v.0.01 (20231217)")
ex_led = machine.Pin(17, machine.Pin.OUT)
in_led = machine.Pin(25, machine.Pin.OUT)
while True:
    for i in range(4):
        ex_led_value = i & 0x01
        in_led_value = i & 0x02
        ex_led.value(ex_led_value)
        in_led.value(in_led_value)
        utime.sleep(0.5)
#    print("GP17 ON")
#    ex_led.value(1)
#    utime.sleep(1)
#    print("GP17 OFF")
#    ex_led.value(0)
#    utime.sleep(1)
    