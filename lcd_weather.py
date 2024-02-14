from machine import Pin, I2C
# need to create ssd1306.py file and upload it to pico manually
import ssd1306

import network
import time
import json
import requests

SSID = 'AkiraHome6-G' # AkiraHome6-G is OK. A is NG
PASSWORD = 'akiragateway0'

def wlan_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    while wlan.status() != 3:
        print("connecting WiFi " + SSID)
        wlan.connect(SSID, PASSWORD)
        max_wait = 10
        while max_wait > 0:
            if wlan.status() < 0 or wlan.status() >= 3:
                break
            max_wait -= 1
            print("wating for connection")
            time.sleep(1)

        if wlan.status() == 3:
            stat = wlan.ifconfig()
            print("connected")
            print("IP = " + stat[0])

            return wlan

        print("retry connection")


# Service: Weather API
# URL: https://www.weatherapi.com/
# Account: gkusumoto+weatherapi@gmail.com
# Password: kud****o
# API Key: 1e4805948bb54c4782021001241402

#https://api.weatherapi.com/v1/current.json?key=1e4805948bb54c4782021001241402&q=Tokyo&aqi=yes
def get_weather():
    API_HOST = 'api.weatherapi.com'
    API_KEY = '1e4805948bb54c4782021001241402'
    URL = f"https://{API_HOST}/v1/current.json?key={API_KEY}&q=Tokyo"

    try:
        response = requests.get(URL)
        #print(response.text)
    except Exception as e:
        print(e)
        raise RuntimeError('failed to get weather')

    weather = json.loads(response.text)
    #print(json.dumps(weather, indent=4))
    return weather


def load_icon():
    file = 'cloudy.dat'
    width = 40
    height = 40
    icon = [0] * (width * height)

    try:
        with open(file, "r") as f:
            print(f"open {file}")
            data = f.read()
            #print(data)
    except OSError as e:
        print(f"open error {file}")
        print(e)
        return icon

    i = 0
    for c in data:
        if c == "\n":
            continue
        try:
            icon[i] = int(c)
        except:
            pass
        i += 1

    return icon

def draw_icon(display: ssd1306.SSD1306, icon_array: list[int] , x: int, y: int):
    i = 0
    width = 40
    height = 40
    for pixel in icon_array:
        xp = i % width
        yp = i // width
        display.pixel(x + xp, y + yp, pixel)
        i += 1

def get_current_hour():
    return time.localtime()[3]

def draw_current_date(display, x, y):
    (year, month, day, _, _, _, _, _) = time.localtime()
    display.text(f"{year:04}-{month:02}-{day:02}", x, y)

def draw_current_time(display, x, y):
    (_, _, _, hour, minute, _, _, _) = time.localtime()
    display.text(f"{hour:02}:{minute:02}", x, y)

wlan = wlan_connect()

LED = Pin("LED", Pin.OUT)
i2c = I2C(0, sda=Pin(16), scl=Pin(17))

addr = i2c.scan()
print("OLED I2C Address = " + hex(addr[0]))

display = ssd1306.SSD1306_I2C(128, 64, i2c)

weather = get_weather()
icon_array = load_icon()
#print(icon_array)
prev_hour = get_current_hour()
while True:
    current_hour = get_current_hour()
    if prev_hour != current_hour:
        print("update weather")
        try:
            weather = get_weather()
            icon_array = load_icon()
            prev_hour = current_hour
        except: pass

    display.fill(0) # delete all

    display.text(weather['current']['condition']['text'], 0, 0, True)

    draw_icon(display, icon_array, 0, 20)
    draw_current_date(display, 44, 24)
    draw_current_time(display, 44, 44)

    display.show() 

    time.sleep(1)
