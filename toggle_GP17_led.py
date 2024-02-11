import machine
import utime

print("Welcome to toggle external LED program v.0.01 (20231217)")
while True:
    machine.Pin(17, machine.Pin.OUT).toggle()
    utime.sleep(1000)