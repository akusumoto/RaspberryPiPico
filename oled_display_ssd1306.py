from machine import Pin, I2C
# need to create ssd1306.py file and upload it to pico manually
import ssd1306
import utime

status = 0
def text():
    global status
    if status == 0:
        status += 1
        return "TEST"
    elif status == 1:
        status += 1
        return "T   "
    elif status == 2:
        status += 1
        return " E  "
    elif status == 3:
        status += 1
        return "  S "
    elif status == 4:
        status = 0
        return "   T"
    else:
        # unknown status
        status = 0
        return "TEST"

LED = Pin("LED", Pin.OUT)
i2c = I2C(0, sda=Pin(16), scl=Pin(17))

addr = i2c.scan()
print("OLED I2C Address = " + hex(addr[0]))

display = ssd1306.SSD1306_I2C(128, 64, i2c)

while True:
    LED.toggle()

    display.fill(0) # delete all

    display.text(text(), 17, 2, True)

    display.show()    

    utime.sleep(1)

print("done")