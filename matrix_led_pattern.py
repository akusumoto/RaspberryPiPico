from machine import Pin
import utime

print("Welcome to Matrix LED program v.0.01 (20231230)")

A01 = 10
A02 = 11
A03 = 12
A04 = 13
A05 = 14
A06 = 15

C01 = 16
C02 = 17
C03 = 18
C04 = 19
C05 = 20

NANODE = 6
NCASODE = 5

ANODES = [
    Pin(A01, Pin.OUT),
    Pin(A02, Pin.OUT),
    Pin(A03, Pin.OUT),
    Pin(A04, Pin.OUT),
    Pin(A05, Pin.OUT),
    Pin(A06, Pin.OUT),
]

CASODES = [
    Pin(C01, Pin.OUT),
    Pin(C02, Pin.OUT),
    Pin(C03, Pin.OUT),
    Pin(C04, Pin.OUT),
    Pin(C05, Pin.OUT),
]

def set_led(led_matrix):
    for c in range(NCASODE):
        CASODES[c].value(0)
        for a in range(NANODE):
            if led_matrix[c][a] > 0:
                ANODES[a].value(1)
            else:
                ANODES[a].value(0)

        for a in range(NANODE):
            ANODES[a].value(0)
        CASODES[c].value(1)

# intialize
def initialize():
    for c in range(NCASODE):
        CASODES[c].value(1)
        for a in range(NANODE):
            ANODES[a].value(0)

# intialize
initialize()


led = [
    [0, 1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1],
    [0, 1, 1, 1, 1, 0],
]

while True:
    set_led(led)

"""
t = utime.ticks_ms()
while True:
    for c in range(NCASODE):
        print(f"C{c}")
        while t + 500 > utime.ticks_ms():
            set_led(led)
        
        t = utime.ticks_ms()
        for cc in range(NCASODE):
            for aa in range(NANODE):
                led[cc][aa] = 1 if cc == c else 0

    for a in range(NANODE):
        print(f"A{a}")
        while t + 500 > utime.ticks_ms():
            set_led(led)
        t = utime.ticks_ms()

        for cc in range(NCASODE):
            for aa in range(NANODE):
                led[cc][aa] = 1 if aa == a else 0
"""