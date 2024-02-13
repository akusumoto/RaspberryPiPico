from machine import Pin
import network
import time

SSID = 'AkiraHome6-G' # AkiraHome6-G is OK. A is NG
PASSWORD = 'akiragateway0'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

print("connecting WiFi " + SSID)
wlan.connect(SSID, PASSWORD)
max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print("wating for connection")
    time.sleep(1)

if wlan.status() != 3:
    raise RuntimeError("network connection failed")
else:
    stat = wlan.ifconfig()
    print("connected")
    print("IP = " + stat[0])
