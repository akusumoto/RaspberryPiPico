import machine
import utime
import max7219

# reference page
# https://microcontrollerslab.com/max7219-led-dot-matrix-display-raspberry-pi-pico/
# 
# max7129 library
# https://github.com/mcauser/micropython-max7219/blob/master/max7219.py

print("LED Matrix with MAX7219")
spi = machine.SPI(0, baudrate=10000000, polarity=1, phase=0, sck=machine.Pin(2), mosi=machine.Pin(3))
cs = machine.Pin(5, machine.Pin.OUT)
cs.value(1)

display = max7219.Matrix8x8(spi, cs, 4)
display.brightness(10)
display.fill(0)
display.show()

while True:
    print("Show 'PICO'")
    display.fill(0)
    display.text('PICO', 0, 0, 1)
    display.show()
    utime.sleep(1)

    print("Show '1234'")
    display.fill(0)
    display.text('1234', 0, 0, 1)
    display.show()
    utime.sleep(1)

    print("Show 'done'")
    display.fill(0)
    display.text('done', 0, 0, 1)
    display.show()
    utime.sleep(1)

    